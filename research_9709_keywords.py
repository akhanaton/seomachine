#!/usr/bin/env python3
"""
Comprehensive keyword research for Cambridge 9709 Pure 1.
Uses DataForSEO API for real data. Outputs prioritised keyword map.
"""

import os, json, base64, requests, time, sys
from datetime import datetime
from collections import defaultdict

# Config
LOGIN = os.getenv('DATAFORSEO_LOGIN', 'apps@exampilot.io')
PASSWORD = os.getenv('DATAFORSEO_PASSWORD', '084f93cd9dc9b32a')
CRED = base64.b64encode(f"{LOGIN}:{PASSWORD}".encode()).decode()
HEADERS = {"Authorization": f"Basic {CRED}", "Content-Type": "application/json"}
BASE = "https://api.dataforseo.com"

# Location codes
LOCATIONS = {
    "UK": 2826,
    "UAE": 2784,
    "Pakistan": 2586,
    "Malaysia": 2458,
    "Singapore": 2702,
    "Nigeria": 2566,
    "Spain": 2724,
    "France": 2250,
    "Germany": 2276,
    "Portugal": 2620,
}

# EU aggregate
EU_LOCATIONS = ["Spain", "France", "Germany", "Portugal"]

# Competitors to analyze
COMPETITORS = [
    "savemyexams.com",
    "physicsandmathstutor.com",
    "papacambridge.com",
]

# Seed keywords for 9709 Pure 1 topics
TOPIC_SEEDS = [
    "cambridge 9709 pure 1",
    "9709 differentiation",
    "9709 integration",
    "9709 trigonometry",
    "9709 vectors",
    "9709 coordinate geometry",
    "9709 functions",
    "9709 quadratics",
    "9709 circular measure",
]

INTENT_SEEDS = [
    "cambridge 9709 past papers",
    "9709 revision guide",
    "how to pass cambridge 9709",
    "cambridge a level maths",
    "a level maths predicted grade",
    "a level maths integration",
    "a level maths differentiation",
    "a level maths revision",
    "a level maths questions by topic",
    "cambridge international a level maths",
]

ALL_SEEDS = TOPIC_SEEDS + INTENT_SEEDS

# Rate limiting
def api_post(endpoint, data):
    """POST with rate limiting."""
    url = f"{BASE}{endpoint}"
    resp = requests.post(url, headers=HEADERS, json=data)
    resp.raise_for_status()
    time.sleep(0.5)  # Rate limit
    return resp.json()

def api_get(endpoint):
    url = f"{BASE}{endpoint}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    time.sleep(0.3)
    return resp.json()

# ============================================================
# PHASE 1: Seed Discovery
# ============================================================

def phase1_competitor_keywords():
    """Pull ranked keywords from competitors filtered to 9709/cambridge."""
    print("\n" + "="*60)
    print("PHASE 1A: Competitor Keyword Stealing")
    print("="*60)
    
    all_competitor_kws = {}
    
    for domain in COMPETITORS:
        print(f"\n--- {domain} ---")
        
        # Try filtering for 9709 keywords
        for filter_term in ["9709", "cambridge maths", "cambridge a level", "pure mathematics"]:
            try:
                data = [{
                    "target": domain,
                    "location_code": 2826,
                    "language_code": "en",
                    "limit": 50,
                    "filters": ["keyword_data.keyword", "like", f"%{filter_term}%"]
                }]
                resp = api_post("/v3/dataforseo_labs/google/ranked_keywords/live", data)
                task = resp['tasks'][0]
                if task['status_code'] == 20000 and task.get('result') and task['result'][0].get('items'):
                    for item in task['result'][0]['items']:
                        kw_data = item.get('keyword_data', {})
                        kw = kw_data.get('keyword', '')
                        vol = kw_data.get('keyword_info', {}).get('search_volume', 0)
                        pos = item.get('ranked_serp_element', {}).get('serp_item', {}).get('rank_absolute', 999)
                        
                        if kw and kw not in all_competitor_kws:
                            all_competitor_kws[kw] = {
                                'keyword': kw,
                                'volume': vol,
                                'source': f"competitor:{domain}",
                                'competitor_position': pos,
                                'competitor_domain': domain,
                            }
                            print(f"  [{filter_term}] {kw}: vol={vol}, pos=#{pos}")
            except Exception as e:
                print(f"  Error for {filter_term}: {e}")
    
    print(f"\n  Total competitor keywords found: {len(all_competitor_kws)}")
    return all_competitor_kws


def phase1_keyword_suggestions():
    """Get keyword suggestions for all seed keywords."""
    print("\n" + "="*60)
    print("PHASE 1B: Keyword Suggestions")
    print("="*60)
    
    all_suggestions = {}
    
    for seed in ALL_SEEDS:
        print(f"\n--- Seed: {seed} ---")
        try:
            data = [{
                "keyword": seed,
                "location_code": 2826,
                "language_code": "en",
                "limit": 20
            }]
            resp = api_post("/v3/dataforseo_labs/google/keyword_suggestions/live", data)
            task = resp['tasks'][0]
            if task['status_code'] == 20000 and task.get('result') and task['result'][0].get('items'):
                for item in task['result'][0]['items']:
                    kw = item.get('keyword', '')
                    vol = item.get('keyword_info', {}).get('search_volume', 0)
                    comp = item.get('keyword_info', {}).get('competition_level', '')
                    
                    if kw and kw not in all_suggestions:
                        all_suggestions[kw] = {
                            'keyword': kw,
                            'volume': vol,
                            'competition': comp,
                            'source': f"suggestion:{seed}",
                        }
                        if vol and vol > 0:
                            print(f"  {kw}: vol={vol}, comp={comp}")
        except Exception as e:
            print(f"  Error: {e}")
    
    print(f"\n  Total suggestions found: {len(all_suggestions)}")
    return all_suggestions


def phase1_serp_questions():
    """Mine question-based keywords."""
    print("\n" + "="*60)
    print("PHASE 1C: Question Mining")
    print("="*60)
    
    question_seeds = [
        "cambridge 9709",
        "a level maths revision",
        "a level maths integration",
        "a level maths differentiation",
        "a level maths exam",
    ]
    
    all_questions = {}
    
    for seed in question_seeds:
        print(f"\n--- Questions for: {seed} ---")
        try:
            data = [{
                "keyword": seed,
                "location_code": 2826,
                "language_code": "en",
                "limit": 30
            }]
            resp = api_post("/v3/dataforseo_labs/google/keyword_suggestions/live", data)
            task = resp['tasks'][0]
            if task['status_code'] == 20000 and task.get('result') and task['result'][0].get('items'):
                for item in task['result'][0]['items']:
                    kw = item.get('keyword', '')
                    vol = item.get('keyword_info', {}).get('search_volume', 0)
                    
                    # Filter for questions
                    if kw and any(kw.lower().startswith(q) for q in ['how', 'what', 'why', 'when', 'can', 'should', 'is', 'are', 'does', 'do', 'will']):
                        all_questions[kw] = {
                            'keyword': kw,
                            'volume': vol,
                            'type': 'question',
                            'source': f"question:{seed}",
                        }
                        print(f"  {kw}: vol={vol}")
        except Exception as e:
            print(f"  Error: {e}")
    
    print(f"\n  Total questions found: {len(all_questions)}")
    return all_questions


# ============================================================
# PHASE 2: Data Enrichment
# ============================================================

def phase2_multi_location_volumes(keywords):
    """Check volumes across target locations."""
    print("\n" + "="*60)
    print("PHASE 2A: Multi-Location Volumes")
    print("="*60)
    
    # Pick top 30 keywords by volume for geo analysis (to manage API costs)
    top_kws = sorted(keywords.values(), key=lambda x: x.get('volume', 0) or 0, reverse=True)[:30]
    kw_list = [k['keyword'] for k in top_kws]
    
    geo_data = {}
    
    for loc_name, loc_code in LOCATIONS.items():
        print(f"\n--- {loc_name} (code: {loc_code}) ---")
        try:
            # Use keyword suggestions with different location to get volumes
            # DataForSEO bulk keyword difficulty gives volumes too
            batch_size = 10
            for i in range(0, len(kw_list), batch_size):
                batch = kw_list[i:i+batch_size]
                data = [{
                    "keywords": batch,
                    "location_code": loc_code,
                    "language_code": "en",
                }]
                resp = api_post("/v3/dataforseo_labs/google/bulk_keyword_difficulty/live", data)
                task = resp['tasks'][0]
                if task['status_code'] == 20000 and task.get('result') and task['result'][0].get('items'):
                    for item in task['result'][0]['items']:
                        kw = item.get('keyword', '')
                        vol = item.get('search_volume', 0)
                        kd = item.get('keyword_difficulty', 0)
                        
                        if kw not in geo_data:
                            geo_data[kw] = {'keyword': kw, 'locations': {}, 'difficulty': kd}
                        geo_data[kw]['locations'][loc_name] = vol
                        
                        if vol and vol > 0:
                            print(f"  {kw}: vol={vol}, kd={kd}")
        except Exception as e:
            print(f"  Error for {loc_name}: {e}")
    
    # Calculate EU aggregate
    print("\n--- EU Aggregate ---")
    for kw, data in geo_data.items():
        eu_vol = sum(data['locations'].get(loc, 0) or 0 for loc in EU_LOCATIONS)
        data['locations']['EU_aggregate'] = eu_vol
        if eu_vol > 0:
            print(f"  {kw}: EU_total={eu_vol}")
    
    return geo_data


# ============================================================
# PHASE 3: Prioritisation
# ============================================================

def phase3_prioritise(all_keywords, geo_data):
    """Score and prioritise all keywords."""
    print("\n" + "="*60)
    print("PHASE 3: Prioritisation")
    print("="*60)
    
    scored = []
    
    for kw, data in all_keywords.items():
        vol = data.get('volume', 0) or 0
        comp = data.get('competition', '')
        
        # Get difficulty from geo_data if available
        kd = 0
        if kw in geo_data:
            kd = geo_data[kw].get('difficulty', 0) or 0
        
        # Score: volume * inverse difficulty * intent bonus
        difficulty_factor = max(1, 100 - (kd or 50)) / 100
        
        # Intent bonus: 9709-specific keywords get 2x weight
        intent_bonus = 1.0
        if '9709' in kw.lower() or 'cambridge' in kw.lower():
            intent_bonus = 2.0
        elif 'pure 1' in kw.lower() or 'pure mathematics' in kw.lower():
            intent_bonus = 1.5
        
        # Question bonus
        if data.get('type') == 'question':
            intent_bonus *= 1.3
        
        priority_score = vol * difficulty_factor * intent_bonus
        
        # Tier assignment
        if kd and kd < 20:
            tier = 'A'  # Quick wins
        elif kd and kd < 35:
            tier = 'B'  # Medium term
        elif vol and vol > 500:
            tier = 'B'  # High volume worth pursuing
        else:
            tier = 'C'  # Long term
        
        # Override: 9709-specific with any volume = Tier A
        if ('9709' in kw.lower() or ('cambridge' in kw.lower() and 'maths' in kw.lower())) and vol and vol > 0:
            tier = 'A'
        
        geo_info = geo_data.get(kw, {}).get('locations', {})
        
        scored.append({
            'keyword': kw,
            'volume_uk': vol,
            'difficulty': kd,
            'competition': comp,
            'priority_score': round(priority_score, 1),
            'tier': tier,
            'intent_bonus': intent_bonus,
            'source': data.get('source', ''),
            'geo': geo_info,
            **{f'vol_{loc.lower()}': geo_info.get(loc, 0) for loc in LOCATIONS},
            'vol_eu': geo_info.get('EU_aggregate', 0),
        })
    
    # Sort by tier then priority score
    tier_order = {'A': 0, 'B': 1, 'C': 2}
    scored.sort(key=lambda x: (tier_order.get(x['tier'], 3), -x['priority_score']))
    
    return scored


# ============================================================
# OUTPUT
# ============================================================

def write_output(scored, geo_data, competitor_kws, output_path):
    """Write the prioritised keyword map."""
    
    tier_a = [k for k in scored if k['tier'] == 'A']
    tier_b = [k for k in scored if k['tier'] == 'B']
    tier_c = [k for k in scored if k['tier'] == 'C']
    
    with open(output_path, 'w') as f:
        f.write(f"# Cambridge 9709 Pure 1 — Keyword Research\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}\n")
        f.write(f"**Data source:** DataForSEO (live API data)\n")
        f.write(f"**Scope:** Cambridge 9709 Pure Mathematics 1 only\n")
        f.write(f"**Locations:** UK, UAE, Pakistan, Malaysia, Singapore, Nigeria, Spain, France, Germany, Portugal\n\n")
        f.write(f"---\n\n")
        
        f.write(f"## Summary\n\n")
        f.write(f"- **Total unique keywords:** {len(scored)}\n")
        f.write(f"- **Tier A (Quick Wins):** {len(tier_a)} keywords\n")
        f.write(f"- **Tier B (Medium Term):** {len(tier_b)} keywords\n")
        f.write(f"- **Tier C (Long Term):** {len(tier_c)} keywords\n")
        f.write(f"- **Competitor keywords stolen:** {len(competitor_kws)}\n")
        f.write(f"- **Total addressable volume (UK):** {sum(k['volume_uk'] or 0 for k in scored):,}/month\n\n")
        
        f.write(f"---\n\n")
        
        # Tier A
        f.write(f"## Tier A — Quick Wins (Write These First)\n\n")
        f.write(f"Low difficulty, 9709-specific. Target for Month 1-2 spokes.\n\n")
        f.write(f"| Keyword | UK Vol | Difficulty | Score | Source |\n")
        f.write(f"|---------|--------|-----------|-------|--------|\n")
        for k in tier_a[:50]:
            f.write(f"| {k['keyword']} | {k['volume_uk'] or 0} | {k['difficulty'] or '?'} | {k['priority_score']} | {k['source'][:30]} |\n")
        
        f.write(f"\n---\n\n")
        
        # Tier B
        f.write(f"## Tier B — Authority Builders (Month 2-3)\n\n")
        f.write(f"Higher volume, moderate difficulty. Build after Tier A establishes presence.\n\n")
        f.write(f"| Keyword | UK Vol | Difficulty | Score | Source |\n")
        f.write(f"|---------|--------|-----------|-------|--------|\n")
        for k in tier_b[:40]:
            f.write(f"| {k['keyword']} | {k['volume_uk'] or 0} | {k['difficulty'] or '?'} | {k['priority_score']} | {k['source'][:30]} |\n")
        
        f.write(f"\n---\n\n")
        
        # Geographic breakdown
        f.write(f"## Geographic Volume Breakdown\n\n")
        f.write(f"Top keywords by location (shows where demand is).\n\n")
        f.write(f"| Keyword | UK | UAE | Pakistan | Malaysia | Singapore | Nigeria | EU (aggregate) |\n")
        f.write(f"|---------|----|----|---------|---------|-----------|---------|----------------|\n")
        geo_kws = [k for k in scored if any(k.get(f'vol_{loc.lower()}', 0) for loc in LOCATIONS)]
        for k in sorted(geo_kws, key=lambda x: x['volume_uk'] or 0, reverse=True)[:30]:
            f.write(f"| {k['keyword'][:40]} | {k.get('vol_uk', 0)} | {k.get('vol_uae', 0)} | {k.get('vol_pakistan', 0)} | {k.get('vol_malaysia', 0)} | {k.get('vol_singapore', 0)} | {k.get('vol_nigeria', 0)} | {k.get('vol_eu', 0)} |\n")
        
        f.write(f"\n---\n\n")
        
        # Competitor gaps
        f.write(f"## Competitor Keywords (Stolen)\n\n")
        f.write(f"Keywords our competitors rank for that we should target.\n\n")
        f.write(f"| Keyword | Competitor | Their Position | UK Vol |\n")
        f.write(f"|---------|-----------|---------------|--------|\n")
        for kw, data in sorted(competitor_kws.items(), key=lambda x: x[1].get('volume', 0) or 0, reverse=True)[:30]:
            f.write(f"| {kw} | {data.get('competitor_domain', '')} | #{data.get('competitor_position', '?')} | {data.get('volume', 0)} |\n")
        
        f.write(f"\n---\n\n")
        
        # Content mapping suggestions
        f.write(f"## Suggested Spoke Articles (Content Map)\n\n")
        f.write(f"Based on keyword clusters. Write in this order.\n\n")
        
        # Group by topic
        topic_groups = defaultdict(list)
        topic_labels = {
            'differentiation': 'Differentiation',
            'integration': 'Integration', 
            'trigonometry': 'Trigonometry',
            'vectors': 'Vectors',
            'coordinate geometry': 'Coordinate Geometry',
            'functions': 'Functions',
            'quadratics': 'Quadratics',
            'circular measure': 'Circular Measure',
            'past paper': 'Past Papers',
            'revision': 'Revision & Strategy',
            'exam': 'Exam Tips',
            'predicted grade': 'Predicted Grade',
        }
        
        for k in tier_a + tier_b:
            kw_lower = k['keyword'].lower()
            assigned = False
            for topic_key, topic_label in topic_labels.items():
                if topic_key in kw_lower:
                    topic_groups[topic_label].append(k)
                    assigned = True
                    break
            if not assigned:
                topic_groups['General / Other'].append(k)
        
        for topic, kws in sorted(topic_groups.items()):
            total_vol = sum(k['volume_uk'] or 0 for k in kws)
            f.write(f"### Spoke: 9709 Pure 1 {topic}\n")
            f.write(f"**Target keywords ({len(kws)}, total vol: {total_vol}/mo):**\n")
            for k in sorted(kws, key=lambda x: x['volume_uk'] or 0, reverse=True)[:8]:
                f.write(f"- {k['keyword']} (vol: {k['volume_uk']}, tier: {k['tier']})\n")
            f.write(f"\n")
        
        f.write(f"\n---\n\n")
        f.write(f"*This research is the foundation for Teresa and Harper's content production.*\n")
        f.write(f"*Use SEO Machine `/research [topic]` for detailed content briefs per article.*\n")
    
    print(f"\n✅ Output written to: {output_path}")


# ============================================================
# MAIN
# ============================================================

def main():
    print("="*60)
    print("CAMBRIDGE 9709 PURE 1 — KEYWORD RESEARCH")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    print("="*60)
    
    # Phase 1
    competitor_kws = phase1_competitor_keywords()
    suggestions = phase1_keyword_suggestions()
    questions = phase1_serp_questions()
    
    # Merge all keywords
    all_keywords = {}
    for source in [competitor_kws, suggestions, questions]:
        for kw, data in source.items():
            if kw not in all_keywords or (data.get('volume', 0) or 0) > (all_keywords[kw].get('volume', 0) or 0):
                all_keywords[kw] = data
    
    print(f"\n\nTotal unique keywords after merge: {len(all_keywords)}")
    
    # Phase 2
    geo_data = phase2_multi_location_volumes(all_keywords)
    
    # Phase 3
    scored = phase3_prioritise(all_keywords, geo_data)
    
    # Output
    output_path = os.path.join(os.path.dirname(__file__), "research", f"9709-pure1-keyword-map-{datetime.now().strftime('%Y-%m-%d')}.md")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    write_output(scored, geo_data, competitor_kws, output_path)
    
    # Also save raw JSON for SEO Machine to use
    json_path = output_path.replace('.md', '.json')
    with open(json_path, 'w') as f:
        json.dump({
            'generated': datetime.now().isoformat(),
            'total_keywords': len(scored),
            'keywords': scored,
            'competitor_keywords': list(competitor_kws.values()),
            'geo_data': {k: v for k, v in geo_data.items()},
        }, f, indent=2)
    print(f"✅ Raw JSON saved to: {json_path}")


if __name__ == '__main__':
    main()
