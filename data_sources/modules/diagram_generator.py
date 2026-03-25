"""
diagram_generator.py — Generate brand-consistent mathematical SVG diagrams.

Uses the ExamPilot colour palette and clean, modern styling suitable for
educational web content. Produces vector SVG output at 10x6 figure size.

Usage:
    python diagram_generator.py [output_directory]

Requires: matplotlib, numpy (add matplotlib>=3.8.0 to requirements.txt)
"""

import os
import math
from pathlib import Path

import matplotlib
matplotlib.use('Agg')  # headless backend — no GUI required

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import numpy as np


# ---------------------------------------------------------------------------
# Brand palette (ExamPilot / Excalidraw)
# ---------------------------------------------------------------------------
BRAND_COLORS = {
    'blue':        '#a5d8ff',
    'blue_dark':   '#339af0',
    'green':       '#b2f2bb',
    'green_dark':  '#2f9e44',
    'orange':      '#ffd8a8',
    'orange_dark': '#e8590c',
    'red':         '#ffc9c9',
    'red_dark':    '#c92a2a',
    'purple':      '#d0bfff',
    'purple_dark': '#7950f2',
    'indigo':      '#dbe4ff',
    'indigo_dark': '#5c7cfa',
    'grey':        '#868e96',
    'grey_light':  '#dee2e6',
    'bg':          '#ffffff',
}

# Ordered list for automatic colour cycling
_CYCLE = [
    BRAND_COLORS['blue_dark'],
    BRAND_COLORS['orange_dark'],
    BRAND_COLORS['green_dark'],
    BRAND_COLORS['purple_dark'],
    BRAND_COLORS['red_dark'],
    BRAND_COLORS['indigo_dark'],
]


class DiagramGenerator:
    """Generate clean, brand-consistent mathematical SVG diagrams."""

    def __init__(self, output_dir: str = '.', brand_colors: dict | None = None):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.colors = brand_colors or BRAND_COLORS
        self._apply_global_style()

    # ------------------------------------------------------------------
    # Global style
    # ------------------------------------------------------------------

    @staticmethod
    def _apply_global_style():
        """Set matplotlib rcParams for a clean, modern look."""
        plt.rcParams.update({
            'font.family':        'sans-serif',
            'font.sans-serif':    ['DejaVu Sans', 'Arial', 'Helvetica', 'sans-serif'],
            'font.size':          12,
            'axes.titlesize':     16,
            'axes.titleweight':   'bold',
            'axes.labelsize':     13,
            'axes.spines.top':    False,
            'axes.spines.right':  False,
            'axes.edgecolor':     BRAND_COLORS['grey'],
            'axes.linewidth':     0.8,
            'axes.grid':          True,
            'grid.color':         BRAND_COLORS['grey_light'],
            'grid.linewidth':     0.5,
            'grid.alpha':         0.7,
            'legend.frameon':     True,
            'legend.framealpha':  0.9,
            'legend.edgecolor':   BRAND_COLORS['grey_light'],
            'legend.fontsize':    12,
            'figure.facecolor':   BRAND_COLORS['bg'],
            'axes.facecolor':     BRAND_COLORS['bg'],
            'savefig.facecolor':  BRAND_COLORS['bg'],
            'figure.figsize':     (10, 6),
            'figure.dpi':         300,
        })

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _save(self, fig, filename: str):
        """Save figure as SVG with tight bounding box."""
        path = self.output_dir / filename
        fig.savefig(str(path), format='svg', bbox_inches='tight', pad_inches=0.3)
        plt.close(fig)
        print(f'  -> {path}')

    @staticmethod
    def _linspace(domain, n=500):
        return np.linspace(domain[0], domain[1], n)

    def _color(self, index: int) -> str:
        return _CYCLE[index % len(_CYCLE)]

    @staticmethod
    def _set_equal_aspect(ax, domain_x, domain_y):
        """Set equal aspect ratio with some padding."""
        ax.set_aspect('equal', adjustable='datalim')
        pad_x = (domain_x[1] - domain_x[0]) * 0.08
        pad_y = (domain_y[1] - domain_y[0]) * 0.08
        ax.set_xlim(domain_x[0] - pad_x, domain_x[1] + pad_x)
        ax.set_ylim(domain_y[0] - pad_y, domain_y[1] + pad_y)

    # ------------------------------------------------------------------
    # 1. Inverse function reflection
    # ------------------------------------------------------------------

    def inverse_function_reflection(
        self, f, f_inv, domain_f, domain_finv,
        label_f, label_finv, key_points,
        filename, title=None,
    ):
        """Draw f(x) and f^{-1}(x) with y=x mirror line and labelled points."""
        fig, ax = plt.subplots()

        # --- curves ---
        x_f = self._linspace(domain_f)
        y_f = np.array([f(xi) for xi in x_f])

        x_fi = self._linspace(domain_finv)
        y_fi = np.array([f_inv(xi) for xi in x_fi])

        ax.plot(x_f, y_f, color=self._color(0), linewidth=2.5, label=label_f, zorder=3)
        ax.plot(x_fi, y_fi, color=self._color(1), linewidth=2.5, label=label_finv, zorder=3)

        # --- y = x mirror ---
        all_vals = np.concatenate([x_f, y_f, x_fi, y_fi])
        lo, hi = float(np.min(all_vals)) - 0.5, float(np.max(all_vals)) + 0.5
        ax.plot([lo, hi], [lo, hi], color=self.colors['grey'], linewidth=1.2,
                linestyle='--', label='y = x', zorder=2)

        # --- key points ---
        for (px, py) in key_points:
            # point on f
            ax.plot(px, py, 'o', color=self._color(0), markersize=8, zorder=4)
            ax.annotate(f'({px}, {py})', (px, py),
                        textcoords='offset points', xytext=(8, 8),
                        fontsize=11, color=self._color(0), fontweight='bold')
            # mirrored point on f_inv
            ax.plot(py, px, 'o', color=self._color(1), markersize=8, zorder=4)
            ax.annotate(f'({py}, {px})', (py, px),
                        textcoords='offset points', xytext=(8, -12),
                        fontsize=11, color=self._color(1), fontweight='bold')
            # connecting dotted line
            ax.plot([px, py], [py, px], ':', color=self.colors['grey'], linewidth=1, zorder=2)

        ax.legend(loc='upper left', fontsize=12)
        if title:
            ax.set_title(title, pad=14)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_aspect('equal', adjustable='datalim')
        self._save(fig, filename)

    # ------------------------------------------------------------------
    # 2. Horizontal shift explanation
    # ------------------------------------------------------------------

    def horizontal_shift_explanation(
        self, f, shift, label_f, filename, title=None,
    ):
        """Visual explanation of why f(x + a) moves LEFT by a units."""
        fig, ax = plt.subplots()

        domain = (-5, 5)
        x = self._linspace(domain)
        y_orig = np.array([f(xi) for xi in x])
        y_shift = np.array([f(xi + shift) for xi in x])

        shifted_label = f'f(x + {shift})'

        ax.plot(x, y_orig, color=self._color(0), linewidth=2.5,
                label=label_f, zorder=3)
        ax.plot(x, y_shift, color=self._color(1), linewidth=2.5,
                label=shifted_label, zorder=3)

        # --- annotation: pick a y-value produced by f, show both x-values ---
        # Use the output at x = 2 for original
        demo_x = 2
        demo_y = f(demo_x)
        shifted_x = demo_x - shift  # same output happens here for f(x+shift)

        # horizontal dashed line at demo_y
        ax.plot([shifted_x, demo_x], [demo_y, demo_y],
                linestyle='--', color=self.colors['grey'], linewidth=1, zorder=2)

        # dots
        ax.plot(demo_x, demo_y, 'o', color=self._color(0), markersize=8, zorder=4)
        ax.plot(shifted_x, demo_y, 'o', color=self._color(1), markersize=8, zorder=4)

        # annotation arrow from original point to shifted point
        ax.annotate(
            '',
            xy=(shifted_x, demo_y + 0.6),
            xytext=(demo_x, demo_y + 0.6),
            arrowprops=dict(
                arrowstyle='->', color=self.colors['red_dark'],
                linewidth=2, connectionstyle='arc3,rad=0.15',
            ),
            zorder=5,
        )
        mid_x = (demo_x + shifted_x) / 2
        ax.text(mid_x, demo_y + 1.6,
                f'{shift} units LEFT',
                ha='center', va='bottom', fontsize=12, fontweight='bold',
                color=self.colors['red_dark'])

        # label the points
        ax.annotate(f'x = {demo_x}\nf({demo_x}) = {demo_y:.0f}',
                     (demo_x, demo_y),
                     textcoords='offset points', xytext=(12, -20),
                     fontsize=10, color=self._color(0))
        ax.annotate(f'x = {shifted_x}\nf({shifted_x}+{shift}) = {demo_y:.0f}',
                     (shifted_x, demo_y),
                     textcoords='offset points', xytext=(-90, -28),
                     fontsize=10, color=self._color(1))

        # explanatory text box
        explanation = (
            f'f(x + {shift}) asks: "what does f see\n'
            f'{shift} units ahead?" — so the\n'
            f'whole curve shifts {shift} units LEFT.'
        )
        ax.text(0.98, 0.97, explanation, transform=ax.transAxes,
                fontsize=11, va='top', ha='right',
                bbox=dict(boxstyle='round,pad=0.5', facecolor=self.colors['orange'],
                          edgecolor=self.colors['orange_dark'], alpha=0.9))

        ax.legend(loc='upper left', fontsize=12)
        if title:
            ax.set_title(title, pad=14)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        self._save(fig, filename)

    # ------------------------------------------------------------------
    # 3. One-one vs many-one (horizontal line test)
    # ------------------------------------------------------------------

    def one_one_vs_many_one(
        self, f_one, f_many, domain_one, domain_many,
        label_one, label_many, filename, title=None,
    ):
        """Side-by-side: one-one (passes HLT) vs many-one (fails HLT)."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        # --- left panel: one-one ---
        x1 = self._linspace(domain_one)
        y1 = np.array([f_one(xi) for xi in x1])
        ax1.plot(x1, y1, color=self._color(0), linewidth=2.5, zorder=3)

        # horizontal test line
        test_y1 = float(f_one((domain_one[0] + domain_one[1]) / 2))
        ax1.axhline(test_y1, color=self.colors['grey'], linestyle='--', linewidth=1.2, zorder=2)

        # find intersection
        from scipy.optimize import brentq  # noqa: delayed import to keep module lightweight
        try:
            ix = brentq(lambda x: f_one(x) - test_y1, domain_one[0], domain_one[1])
            ax1.plot(ix, test_y1, 'o', color=self.colors['green_dark'], markersize=10, zorder=4)
            ax1.annotate('1 intersection',
                         (ix, test_y1), textcoords='offset points', xytext=(10, 10),
                         fontsize=11, color=self.colors['green_dark'], fontweight='bold')
        except Exception:
            pass

        ax1.set_title(label_one, fontsize=14, color=self.colors['green_dark'])
        ax1.text(0.5, 0.02, 'PASSES horizontal line test',
                 transform=ax1.transAxes, ha='center', fontsize=11,
                 color=self.colors['green_dark'], fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=self.colors['green'],
                           edgecolor=self.colors['green_dark'], alpha=0.85))
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')

        # --- right panel: many-one ---
        x2 = self._linspace(domain_many)
        y2 = np.array([f_many(xi) for xi in x2])
        ax2.plot(x2, y2, color=self._color(1), linewidth=2.5, zorder=3)

        # horizontal test line — choose a y that crosses twice
        y_mid = float(f_many(domain_many[1] * 0.6))
        ax2.axhline(y_mid, color=self.colors['grey'], linestyle='--', linewidth=1.2, zorder=2)

        # find intersections
        intersections = []
        xs = self._linspace(domain_many, 2000)
        ys = np.array([f_many(xi) - y_mid for xi in xs])
        for i in range(len(ys) - 1):
            if ys[i] * ys[i + 1] < 0:
                try:
                    root = brentq(lambda x: f_many(x) - y_mid, float(xs[i]), float(xs[i + 1]))
                    intersections.append(root)
                except Exception:
                    pass

        for ix_val in intersections:
            ax2.plot(ix_val, y_mid, 'o', color=self.colors['red_dark'], markersize=10, zorder=4)

        if len(intersections) >= 2:
            ax2.annotate(f'{len(intersections)} intersections',
                         (intersections[-1], y_mid),
                         textcoords='offset points', xytext=(10, 10),
                         fontsize=11, color=self.colors['red_dark'], fontweight='bold')

        ax2.set_title(label_many, fontsize=14, color=self.colors['red_dark'])
        ax2.text(0.5, 0.02, 'FAILS horizontal line test',
                 transform=ax2.transAxes, ha='center', fontsize=11,
                 color=self.colors['red_dark'], fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=self.colors['red'],
                           edgecolor=self.colors['red_dark'], alpha=0.85))
        ax2.set_xlabel('x')
        ax2.set_ylabel('y')

        if title:
            fig.suptitle(title, fontsize=16, fontweight='bold', y=1.02)

        fig.tight_layout()
        self._save(fig, filename)

    # ------------------------------------------------------------------
    # 4. Generic single transformation
    # ------------------------------------------------------------------

    def function_transformation(
        self, f, transform_f, domain,
        label_original, label_transformed,
        transform_description, filename, title=None,
    ):
        """Show original f(x) and one transformed version on the same axes."""
        fig, ax = plt.subplots()

        x = self._linspace(domain)
        y_orig = np.array([f(xi) for xi in x])
        y_trans = np.array([transform_f(xi) for xi in x])

        ax.plot(x, y_orig, color=self._color(0), linewidth=2.5,
                label=label_original, zorder=3)
        ax.plot(x, y_trans, color=self._color(1), linewidth=2.5,
                label=label_transformed, zorder=3)

        ax.text(0.98, 0.97, transform_description, transform=ax.transAxes,
                fontsize=11, va='top', ha='right',
                bbox=dict(boxstyle='round,pad=0.5', facecolor=self.colors['indigo'],
                          edgecolor=self.colors['indigo_dark'], alpha=0.85))

        ax.legend(loc='upper left', fontsize=12)
        if title:
            ax.set_title(title, pad=14)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        self._save(fig, filename)

    # ------------------------------------------------------------------
    # 5. Transformation grid (2x2 or 2x3)
    # ------------------------------------------------------------------

    def transformation_grid(
        self, f, domain, transformations, filename, title=None,
    ):
        """Grid of transformations of the same base function.

        Args:
            transformations: list of dicts with keys:
                'func'        — callable
                'label'       — e.g. "y = f(x) + 2"
                'description' — e.g. "Shift up by 2"
                'color'       — optional colour override
        """
        n = len(transformations)
        cols = min(n, 3)
        rows = math.ceil(n / cols)
        fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 5 * rows))
        if n == 1:
            axes = [axes]
        else:
            axes = axes.flatten()

        x = self._linspace(domain)
        y_base = np.array([f(xi) for xi in x])

        for i, t in enumerate(transformations):
            ax = axes[i]
            y_t = np.array([t['func'](xi) for xi in x])
            color = t.get('color', self._color(i))

            ax.plot(x, y_base, color=self.colors['grey'], linewidth=1.5,
                    linestyle='--', label='f(x)', zorder=2)
            ax.plot(x, y_t, color=color, linewidth=2.5,
                    label=t['label'], zorder=3)

            ax.set_title(t['description'], fontsize=13, pad=8)
            ax.legend(loc='upper left', fontsize=10)
            ax.set_xlabel('x', fontsize=10)
            ax.set_ylabel('y', fontsize=10)

        # hide unused axes
        for j in range(n, len(axes)):
            axes[j].set_visible(False)

        if title:
            fig.suptitle(title, fontsize=16, fontweight='bold', y=1.02)

        fig.tight_layout()
        self._save(fig, filename)

    # ------------------------------------------------------------------
    # 6. Generic curves with annotations
    # ------------------------------------------------------------------

    def curve_with_annotations(
        self, curves, annotations, domain, filename, title=None,
    ):
        """Plot one or more curves with text/arrow annotations.

        Args:
            curves: list of dicts with keys:
                'func'  — callable
                'label' — legend label
                'color' — optional
                'style' — optional line style (default '-')
            annotations: list of dicts with keys:
                'text'       — annotation text
                'xy'         — (x, y) point to annotate
                'xytext'     — (x, y) text position
                'arrowprops' — optional dict (defaults to brand arrow)
            domain: (xmin, xmax)
        """
        fig, ax = plt.subplots()
        x = self._linspace(domain)

        for i, c in enumerate(curves):
            y = np.array([c['func'](xi) for xi in x])
            color = c.get('color', self._color(i))
            style = c.get('style', '-')
            ax.plot(x, y, color=color, linewidth=2.5, linestyle=style,
                    label=c.get('label', ''), zorder=3)

        for ann in annotations:
            props = ann.get('arrowprops', dict(
                arrowstyle='->', color=self.colors['grey'], linewidth=1.5,
            ))
            ax.annotate(
                ann['text'], xy=ann['xy'], xytext=ann['xytext'],
                fontsize=11, fontweight='bold',
                arrowprops=props, zorder=5,
            )

        ax.legend(fontsize=12)
        if title:
            ax.set_title(title, pad=14)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        self._save(fig, filename)

    # ------------------------------------------------------------------
    # 7. Shaded area between curves
    # ------------------------------------------------------------------

    def shaded_area(
        self, f, g, x_range, filename, title=None,
        shade_color=None, label_f=None, label_g=None,
    ):
        """Shade the area between two curves (useful for integration).

        Args:
            f: upper curve callable (or None for x-axis, i.e. y=0)
            g: lower curve callable (or None for x-axis, i.e. y=0)
            x_range: (a, b) integration limits
        """
        fig, ax = plt.subplots()

        pad = (x_range[1] - x_range[0]) * 0.5
        full_domain = (x_range[0] - pad, x_range[1] + pad)
        x_full = self._linspace(full_domain)
        x_shade = self._linspace(x_range)

        f_vals_full = np.array([f(xi) for xi in x_full]) if f else np.zeros_like(x_full)
        g_vals_full = np.array([g(xi) for xi in x_full]) if g else np.zeros_like(x_full)
        f_vals_shade = np.array([f(xi) for xi in x_shade]) if f else np.zeros_like(x_shade)
        g_vals_shade = np.array([g(xi) for xi in x_shade]) if g else np.zeros_like(x_shade)

        s_color = shade_color or self.colors['blue']

        if f:
            ax.plot(x_full, f_vals_full, color=self._color(0), linewidth=2.5,
                    label=label_f or 'f(x)', zorder=3)
        if g:
            ax.plot(x_full, g_vals_full, color=self._color(1), linewidth=2.5,
                    label=label_g or 'g(x)', zorder=3)

        ax.fill_between(x_shade, f_vals_shade, g_vals_shade,
                         color=s_color, alpha=0.4, zorder=2)

        # vertical dashed lines at limits
        for bnd in x_range:
            ax.axvline(bnd, color=self.colors['grey'], linestyle=':', linewidth=1, zorder=1)

        ax.legend(fontsize=12)
        if title:
            ax.set_title(title, pad=14)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        self._save(fig, filename)

    # ------------------------------------------------------------------
    # 8. Stationary points diagram
    # ------------------------------------------------------------------

    def stationary_points_diagram(
        self, f, f_prime, domain, stat_points, filename, title=None,
    ):
        """Show a curve with classified stationary points.

        Args:
            stat_points: list of dicts with:
                'x'    — x-coordinate
                'type' — 'max', 'min', or 'inflection'
        """
        fig, ax = plt.subplots()

        x = self._linspace(domain)
        y = np.array([f(xi) for xi in x])
        ax.plot(x, y, color=self._color(0), linewidth=2.5, zorder=3)

        type_styles = {
            'max':        {'color': self.colors['red_dark'],    'marker': 'v', 'label': 'Maximum'},
            'min':        {'color': self.colors['green_dark'],  'marker': '^', 'label': 'Minimum'},
            'inflection': {'color': self.colors['purple_dark'], 'marker': 's', 'label': 'Inflection'},
        }

        labelled_types = set()
        for sp in stat_points:
            sx = sp['x']
            sy = f(sx)
            stype = sp['type']
            style = type_styles.get(stype, type_styles['inflection'])

            lbl = style['label'] if stype not in labelled_types else None
            labelled_types.add(stype)

            ax.plot(sx, sy, marker=style['marker'], color=style['color'],
                    markersize=12, zorder=5, label=lbl, markeredgecolor='white',
                    markeredgewidth=1.5)

            offset_y = 12 if stype == 'min' else -16
            ax.annotate(
                f'{style["label"]}\n({sx:.1f}, {sy:.1f})',
                (sx, sy),
                textcoords='offset points', xytext=(14, offset_y),
                fontsize=10, color=style['color'], fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=style['color'], linewidth=1.2),
            )

            # tangent line at stationary point (slope = 0)
            tangent_w = (domain[1] - domain[0]) * 0.08
            ax.plot([sx - tangent_w, sx + tangent_w], [sy, sy],
                    color=style['color'], linewidth=1.5, linestyle='--', zorder=4)

        ax.legend(fontsize=11)
        if title:
            ax.set_title(title, pad=14)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        self._save(fig, filename)


    # ------------------------------------------------------------------
    # 9. Trig transformation steps (sequential)
    # ------------------------------------------------------------------

    def trig_transformation_steps(
        self, steps, domain, filename, title=None,
    ):
        """Show sequential transformations of a trig function.

        Each subplot shows the original (dashed) and the cumulative
        transformation at that step (solid).

        Args:
            steps: list of dicts with keys:
                'func'        — callable for the curve at this step
                'label'       — e.g. "y = cos(x − π/3)"
                'description' — e.g. "Shift right by π/3"
            domain: (xmin, xmax)
        """
        n = len(steps)
        fig, axes = plt.subplots(1, n, figsize=(5 * n, 5))
        if n == 1:
            axes = [axes]

        x = self._linspace(domain, n=500)
        y_base = np.array([steps[0]['func'](xi) for xi in x])

        for i, step in enumerate(steps):
            ax = axes[i]
            y_step = np.array([step['func'](xi) for xi in x])

            # always show original cos(x) as dashed grey
            y_orig = np.array([np.cos(xi) for xi in x])
            ax.plot(x, y_orig, color=self.colors['grey'], linewidth=1.5,
                    linestyle='--', label='y = cos x', zorder=2, alpha=0.6)

            # show previous step as light dashed if not the first step
            if i > 0:
                y_prev = np.array([steps[i - 1]['func'](xi) for xi in x])
                ax.plot(x, y_prev, color=self._color(i - 1), linewidth=1.5,
                        linestyle=':', label=steps[i - 1]['label'], zorder=2,
                        alpha=0.5)

            ax.plot(x, y_step, color=self._color(i), linewidth=2.5,
                    label=step['label'], zorder=3)

            ax.set_title(f"Step {i + 1}: {step['description']}",
                         fontsize=12, pad=8, fontweight='bold')
            ax.legend(loc='upper right', fontsize=9)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_ylim(-3.5, 4.5)
            ax.axhline(0, color=self.colors['grey_light'], linewidth=0.5)

        if title:
            fig.suptitle(title, fontsize=16, fontweight='bold', y=1.02)

        fig.tight_layout()
        self._save(fig, filename)


# ======================================================================
# CLI entry point — generate sample diagrams
# ======================================================================

if __name__ == '__main__':
    import sys

    output_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    gen = DiagramGenerator(output_dir)

    print('Generating diagrams...')

    # Diagram 1: Inverse function reflection
    # f(x) = x^2 for x >= 0, f^-1(x) = sqrt(x)
    gen.inverse_function_reflection(
        f=lambda x: x**2,
        f_inv=lambda x: np.sqrt(x),
        domain_f=(0, 3),
        domain_finv=(0, 9),
        label_f='f(x) = x\u00b2, x \u2265 0',
        label_finv='f\u207b\u00b9(x) = \u221ax',
        key_points=[(1, 1), (2, 4)],
        filename='functions-inverse-reflection.svg',
        title='f(x) and f\u207b\u00b9(x) \u2014 Reflection in y = x',
    )

    # Diagram 2: Why f(x+3) moves left
    gen.horizontal_shift_explanation(
        f=lambda x: x**2,
        shift=3,
        label_f='f(x) = x\u00b2',
        filename='functions-horizontal-shift-explained.svg',
        title='Why Does f(x + 3) Move LEFT?',
    )

    # Diagram 3: One-one vs many-one
    gen.one_one_vs_many_one(
        f_one=lambda x: 2 * x + 1,
        f_many=lambda x: x**2,
        domain_one=(-2, 3),
        domain_many=(-2.5, 2.5),
        label_one='f(x) = 2x + 1\n(one-one)',
        label_many='f(x) = x\u00b2\n(many-one)',
        filename='functions-one-one-vs-many-one.svg',
        title='The Horizontal Line Test: One-One vs Many-One',
    )

    # ----- Integration diagrams -----

    # Diagram 4: Area under a curve (definite integral)
    gen.shaded_area(
        f=lambda x: -x**2 + 4*x,
        g=None,  # x-axis
        x_range=(1, 3),
        filename='integration-area-under-curve.svg',
        title='Definite Integral: Area Under a Curve',
        label_f='y = -x\u00b2 + 4x',
    )

    # Diagram 5: Area between a curve and a line
    gen.shaded_area(
        f=lambda x: -x**2 + 6*x - 3,
        g=lambda x: x + 1,
        x_range=(1, 4),
        filename='integration-area-between-curves.svg',
        title='Area Between a Curve and a Line',
        label_f='y = -x\u00b2 + 6x - 3',
        label_g='y = x + 1',
    )

    # Diagram 6: Negative area trap (curve crossing x-axis)
    def curve_crosses(x):
        return x**3 - 3*x

    fig, ax = plt.subplots()
    x_full = np.linspace(-2.5, 2.5, 500)
    y_full = np.array([curve_crosses(xi) for xi in x_full])
    ax.plot(x_full, y_full, color=gen._color(0), linewidth=2.5, label='y = x\u00b3 - 3x', zorder=3)

    # positive area (above x-axis): approx -sqrt(3) to 0
    s3 = np.sqrt(3)
    x_pos = np.linspace(-s3, 0, 200)
    y_pos = np.array([curve_crosses(xi) for xi in x_pos])
    ax.fill_between(x_pos, y_pos, 0, color=gen.colors['green'], alpha=0.5, zorder=2,
                     label='Positive area')

    # negative area (below x-axis): 0 to sqrt(3)
    x_neg = np.linspace(0, s3, 200)
    y_neg = np.array([curve_crosses(xi) for xi in x_neg])
    ax.fill_between(x_neg, y_neg, 0, color=gen.colors['red'], alpha=0.5, zorder=2,
                     label='Negative area')

    ax.axhline(0, color=gen.colors['grey'], linewidth=0.8, zorder=1)

    # annotations
    ax.annotate('This area is\nPOSITIVE', xy=(-1, 0.8), fontsize=11,
                color=gen.colors['green_dark'], fontweight='bold', ha='center')
    ax.annotate('This area is\nNEGATIVE', xy=(1, -0.8), fontsize=11,
                color=gen.colors['red_dark'], fontweight='bold', ha='center')

    # warning box
    ax.text(0.98, 0.97,
            'If the curve crosses the x-axis,\nsplit the integral at the roots\nand take absolute values.',
            transform=ax.transAxes, fontsize=11, va='top', ha='right',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=gen.colors['orange'],
                      edgecolor=gen.colors['orange_dark'], alpha=0.9))

    ax.legend(loc='lower left', fontsize=11)
    ax.set_title('The Negative Area Trap', fontsize=16, fontweight='bold', pad=14)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    gen._save(fig, 'integration-negative-area-trap.svg')

    # ----- Trigonometry diagrams -----

    # Diagram 7: Sequential trig transformation (cos x → 2cos(x - π/3) + 1)
    pi = np.pi
    gen.trig_transformation_steps(
        steps=[
            {
                'func': lambda x: np.cos(x - pi / 3),
                'label': 'y = cos(x − π/3)',
                'description': 'Shift right by π/3',
            },
            {
                'func': lambda x: 2 * np.cos(x - pi / 3),
                'label': 'y = 2cos(x − π/3)',
                'description': 'Vertical stretch ×2',
            },
            {
                'func': lambda x: 2 * np.cos(x - pi / 3) + 1,
                'label': 'y = 2cos(x − π/3) + 1',
                'description': 'Shift up by 1',
            },
        ],
        domain=(0, 2 * pi),
        filename='trig-graph-transformation-steps.svg',
        title='Building y = 2cos(x − π/3) + 1 from y = cos x',
    )

    print(f'Generated 7 diagrams in {output_dir}')
