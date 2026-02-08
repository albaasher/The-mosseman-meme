# Mooseman Driving - Development Versions

This branch contains intermediate versions created during development.

## Files

### `mooseman_mobile_first.html`
- Mobile-first rebuild attempt
- Uses percentage-based coordinates instead of pixels
- Designed to scale to any screen size
- **Issues:** Subtitle positioning was difficult, path scaling inconsistent

### `mooseman_subtitles_locked.html`
- Introduced `canvasToScreen()` function
- Fixed subtitle positioning to follow car correctly
- Uses canvas getBoundingClientRect() for proper scaling
- **Issues:** Mobile viewport problems, subtitles sometimes off-screen

### `mooseman_no_audio.html`
- Working version without audio functionality
- Clean subtitle implementation
- Fixed width canvas (1200x800)
- **Status:** Fully functional, just missing audio sync

## Evolution
1. Started with Python turtle graphics
2. Converted to HTML/Canvas
3. Fixed mobile scaling issues
4. Added subtitle synchronization
5. Added audio with delay timing
6. Final version → moved to `main` branch

## Notes
These versions are kept for documenting purposes. For the final working version, see the `main` branch.

*Claude did most of the heavy lefting but most regarding where and how the lines are displayed and how the car moves and also the timing of the subtitles was done manually*
