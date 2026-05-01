---
name: Gregory Duane
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#1a1a1a'
  on-primary-container: '#848282'
  inverse-primary: '#5f5e5e'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c6c6c6'
  on-tertiary: '#2f3131'
  tertiary-container: '#191a1b'
  on-tertiary-container: '#828383'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.2em
spacing:
  unit: 8px
  gutter: 24px
  margin: 64px
  section-gap: 128px
  max-width: 1440px
---

## Brand & Style

This design system embodies the peak of sartorial excellence, channeling the cinematic and editorial aesthetics of high-fashion icons. The brand personality is authoritative yet understated, reflecting the precision of a bespoke tailor’s stitch. It caters to a discerning clientele who values heritage, exclusivity, and a "quiet luxury" philosophy.

The design style is **Minimalist-Cinematic**. It leverages "darkspace" to create an atmosphere of intimacy and prestige. Visuals are treated as editorial spreads, where the interface recedes to allow high-fidelity photography of textiles and craftsmanship to take center stage. The emotional response is one of calm confidence and timeless sophistication.

## Colors

The palette is rooted in a deep, atmospheric foundation. The primary color is a rich charcoal (#1A1A1A), used as the primary canvas to create depth. Pure white is utilized sparingly for high-contrast legibility and razor-sharp accents.

Metallic accents provide the necessary warmth and prestige:
- **Primary:** Charcoal Black for the environment and "darkspace."
- **Secondary:** Polished Gold (#D4AF37) for premium calls to action and heritage highlights.
- **Tertiary:** Brushed Silver (#C0C0C0) for subtle UI dividers and secondary metadata.
- **Neutral:** Stark White (#FFFFFF) for primary text and brand-critical information.

## Typography

This design system employs a high-contrast typographic pairing to mirror the duality of traditional tailoring and modern luxury.

**Noto Serif** is the headline face, evoking the intellectual and authoritative feel of a heritage fashion masthead. It should be used for all large-scale editorial moments.

**Manrope** provides a clean, refined sans-serif counterpoint for body copy and functional UI. Its modern proportions ensure clarity on dark backgrounds. 

**Formatting Note:** "Label-caps" should be used for navigational elements and small headers to inject a sense of structure and luxury branding. A script font (Tangerine) can be used for signature-style accents or personalized notes to the user, but should never be used for functional interface elements.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model with generous, intentional margins that create an "island" effect for content. This maximizes the feeling of exclusivity and focus.

- **The Grid:** A 12-column system with a generous 24px gutter.
- **Darkspace:** Generous vertical rhythm (Section Gaps) of 128px or more between major content blocks to allow the eye to rest and emphasize the importance of each section.
- **Imagery:** Photography should often break the grid or span 100% of the viewport width to create a cinematic, immersive experience.

## Elevation & Depth

In a dark-mode-first environment, depth is achieved through **Tonal Layers** and light rather than shadows. 

1.  **Base:** The primary charcoal background (#1A1A1A).
2.  **Raised Surfaces:** A slightly lighter tint of charcoal used for cards or containers to suggest they are closer to the viewer.
3.  **Ghost Outlines:** Instead of heavy shadows, use ultra-thin (1px) borders in silver or low-opacity white to define edges.
4.  **Luminescence:** Use gold-tinted outer glows sparingly on primary call-to-action elements to simulate the way light catches metallic thread or jewelry.

## Shapes

The shape language is **Sharp (0)**. In the world of bespoke tailoring, precision is paramount. Every UI element—from buttons to image containers—features 90-degree corners. 

Sharp edges communicate a sense of architectural structure and formal elegance. This lack of rounding differentiates the product from more approachable, consumer-grade apps and aligns it with the heritage aesthetics of luxury houses like Armani and Tom Ford.

## Components

### Buttons
Primary buttons are stark white with black text, featuring no border-radius. Hover states should transition to the Gold accent. Secondary buttons are "Ghost" style—sharp 1px silver borders with uppercase, letter-spaced text.

### Input Fields
Inputs are minimalist underlines rather than boxes. When focused, the silver underline should transition to gold with a subtle, shimmering animation.

### Cards
Cards for garments or collections should be borderless, using large-scale imagery that fills the container. Typography should be overlaid using a subtle gradient scrim to ensure legibility while maintaining the cinematic feel.

### Navigation
The navigation should be centered and airy, using the "label-caps" typographic style. Use high-contrast transitions where the logo remains static while the background or imagery scrolls beneath it.

### Editorial Accents
Include "Lookbook" components that allow for asymmetric image clusters, mimicking a physical fashion magazine layout. Use Noto Serif for large pull-quotes that serve as artistic dividers.