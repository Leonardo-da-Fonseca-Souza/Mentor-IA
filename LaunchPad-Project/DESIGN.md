# LaunchPad Design System (Orbital Kinetic)

This design system is tailored for modern, high-tech aerospace interfaces. It combines **Modern Minimalism** with **Glassmorphism**, leveraging dark surfaces representing the vacuum of space with high-energy luminous accents.

---

## 🎨 Color Palette

The palette is anchored in a dark cosmic environment with vibrant high-energy accent colors indicating interaction and data status.

### Brand Colors
| Role | Color | Preview | Description |
| :--- | :--- | :--- | :--- |
| **Primary** | `#ebb2ff` | `████████` | Neon Purple. Primary CTAs, mission-critical status indicators. |
| **Secondary** | `#a2e7ff` | `████████` | Electric Blue. Secondary actions, data visualization, hover states. |
| **Surface** | `#101415` | `████████` | Deep Navy/Slate. Background for cards and elevated panels. |
| **Background** | `#101415` | `████████` | The core dark background representing space. |
| **Outline** | `#9d8ba0` | `████████` | Muted border outlines. |

### Semantic & System Colors
*   **Error:** `#ffb4ab` (On Error: `#690005`)
*   **Error Container:** `#93000a` (On Error Container: `#ffdad6`)
*   **Tertiary:** `#c4c6cf` (Tertiary Container: `#74767e`)
*   **Surface Bright:** `#363a3b`
*   **Surface Container (Highest):** `#323537`
*   **Surface Container (Lowest):** `#0b0f10`

---

## font Typography

A dual-font system is employed to balance geometric industrial aesthetics with high technical legibility.
*   **Display Font:** `Sora` (Used for major headings, technical metrics, and hero sections)
*   **Body/Functional Font:** `Inter` (Used for reading, controls, navigation, and data grids)

### Typographic Scales

| Name | Font Family | Size | Weight | Line Height | Letter Spacing |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **display-lg** | Sora | 72px | 700 | 80px | `-0.02em` |
| **display-lg-mobile** | Sora | 40px | 700 | 48px | `-0.01em` |
| **headline-lg** | Sora | 48px | 600 | 56px | `-0.01em` |
| **headline-md** | Sora | 32px | 600 | 40px | — |
| **body-lg** | Inter | 18px | 400 | 28px | — |
| **body-md** | Inter | 16px | 400 | 24px | — |
| **label-caps** | Inter | 12px | 600 | 16px | `0.1em` |
| **mono-label** | Inter | 14px | 500 | 20px | `0.02em` |

---

## 📐 Layout & Roundness

Derived from a clean 8px spacing unit.

*   **Base Spacing Unit:** `8px`
*   **Container Max-Width:** `1280px`
*   **Gutter:** `24px`
*   **Margins:** `64px` (Desktop) / `16px` (Mobile)
*   **Corner Radii:**
    *   `sm`: `0.125rem` (2px)
    *   `DEFAULT`: `0.25rem` (4px) — standard sharp controls
    *   `md`: `0.375rem` (6px)
    *   `lg`: `0.5rem` (8px) — interactive elements
    *   `xl`: `0.75rem` (12px) — container panels & glass cards
    *   `full`: `9999px` — status pills / badges
