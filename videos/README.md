# Videos Folder

This folder is intended for video animations created with Manim (Mathematical Animation Engine) that visualize concepts from the Canonical Core framework.

## Status

**Note:** The video files are not currently included in this repository. The videos were created previously but are excluded from version control due to their large file size (approximately 566 video files). To obtain the videos, please contact the repository maintainer or check for external hosting links in future releases.

## Planned Contents

The videos would be organized into the following directories:

### Adaptive-π Related
- **adaptive_pi_manim_dual/** - Dual view animations of adaptive π concepts
- **adaptive_pi_scaling_manim/** - Scaling behavior of adaptive π

### Holonomy and Surfaces
- **holonomy_surface_equation_manim/** - Holonomy surface equations
- **prroot_holonomy_surfaces_manim/** - PR-Root holonomy surfaces

### Phase Spine
- **phase_spine/** - Primary phase spine animations at 1080p60
- **phase_spine (2)/** - Alternative phase spine rendering
- **phase_spine (2) - Copy/** - Phase spine backup/variant
- **phase_spine - Copy/** - Phase spine alternative at 1080p60

### Quantum and Geometric Concepts
- **fibonacci_chsh_manim/** - Fibonacci CHSH inequality
- **lightcone_fibonacci_sampling_manim/** - Light cone Fibonacci sampling
- **tape_waveplates_jones_manim/** - Tape waveplates using Jones calculus
- **z2_manim_dashboard/** - Z2 dashboard visualization

### Other
- **attractor_switch/** - Attractor switch 3D animation
- **pr_root_vibe_explainer_manim/** - PR-Root vibe explainer

## Video Format

Videos are rendered in different formats depending on their complexity and purpose:
- **480p15**: 480p resolution at 15fps (most Manim animations)
- **1080p60**: 1080p resolution at 60fps (phase_spine and z2_manim_dashboard)

Each directory typically contains:
- Main animation files (`.mp4`)
- `partial_movie_files/` subdirectory with intermediate render files from Manim's compilation process

## Total Files

The complete collection would contain approximately 566 video files across all animations.

## Note

These video files are excluded from version control via `.gitignore` to keep the repository size manageable. If you need access to the video files, please open an issue or contact the repository maintainer to discuss hosting options (e.g., external cloud storage, GitHub releases, or generation from source scripts).
