---
adapter: svg
max_iters: 8
score_threshold: 0.9
no_improvement_for: 5
---

# Mechanical Pocket Watch                                                                                                                                                                                                                                 

Draw a detailed mechanical pocket watch, viewed from the front, centered                                                                                                                                                                                
in a 600×600 viewBox. The watch must include ALL of the following:

## Case & Crown                                                                                                                                                                                                                                            
- A circular outer case (radius ~200) with a metallic gradient fill                                                                                                                                                                                        
- A crown (winder knob) at the top (12 o'clock position) attached to a                                                                                                                                                                                     
short stem that extends into the case                                                                                                                                                                                                                      
- A subtle bezel ring around the outer edge                                                                                                                                                                                                                 

## Dial                                                                                                                                                                                                                                                    
- A white or cream-colored dial face (radius ~170) with a semi-transparent lower half (or a clip-path cutout) to reveal the movement gears beneath.                                                                                                                                                         
- 12 hour markers: thick lines at 12, 3, 6, 9 o'clock; thinner lines at                                                                                                                                                                                     
the other hours                                                                                                                                                                                                                                            
- 12 Roman numerals (I through XII) positioned just inside the hour markers. All 12 numerals must be clearly visible and legible.                                                                                                                                                                                
- Minute tick marks around the outer edge of the dial (exactly 60 ticks, spaced every 6°).

## Hands                                                                                                                                                                                                                                                  
- An hour hand (shorter, thicker) pointing near the 10 o'clock position (rotated 300° from 12 o'clock).                                                                                                                                                 
- A minute hand (longer, thinner) pointing near the 2 o'clock position (rotated 60° from 12 o'clock).                                                                                                                                                     
- A thin second hand (red or dark) pointing exactly to the 7 o'clock position (rotated 210° from 12 o'clock).                                                                                                                                              
- All three hands originating from the exact center of the dial                                                                                                                                                                                             

## Sub-dials                                                                                                                                                                                                                                              
- A small seconds sub-dial at the 6 o'clock position (radius ~30) with                                                                                                                                                                    
its own tiny hand colored red or black.                                                                                                                                                                                                                    
- A power reserve indicator sub-dial at the 12 o'clock position (radius ~25)                                                                                                                                                                                
with an arc showing ~60% charge. This sub-dial must be clearly rendered.

## Movement (visible through caseback or cutaway)                                                                                                                                                                                                        
- At least 3 visible gears of different sizes with teeth, positioned                                                                                                                                                                                        
below the dial area (bottom half of the watch). The gears must be rendered with high opacity (>= 0.8) to ensure they are clearly visible and not washed out.                                                                                               
- The gears should overlap realistically and show different sizes                                                                                                                                                                                        
(large, medium, small)                                                                                                                                                                                                                                   
- A balance wheel visible near the bottom-right of the movement area                                                                                                                                                                                      

## Chain                                                                                                                                                                                                                                                 
- A short chain of 3-4 distinct, interlocking oval links attached to the crown, curving upward and                                                                                                                                                             
outward from the top of the watch. The chain must be clearly visible and distinct.

## Style                                                                                                                                                                                                                                                 
- Metallic/brass color palette for the case and gears                                                                                                                                                                                                    
- Clean line art with subtle shading                                                                                                                                                                                                                     
- The entire composition must be centered and balanced                                                                                                                                                                                                   
- The SVG must parse as valid XML                                                                                                                                                                                                                        

The result should look like a realistic, detailed illustration of a                                                                                                                                                                                       
vintage mechanical pocket watch — not a cartoon or simplified icon.

## Iteration history
- iter 0: Resolve the front-view versus movement visibility contradiction by layering a semi-transparent lower dial over the exposed gears, ensuring all hands, markers, and sub-dials align precisely to the 300,300 center. → Expected outcome: A coherent, directly renderable composition that satisfies every structural requirement without deferring to meta-planning.
- iter 1: Add the missing chain attached to the crown, complete all 12 Roman numerals, and implement the power reserve indicator sub-dial at the 12 o'clock position. → Expected outcome: A fully compliant watch illustration with all required components present.
- iter 2: Enforce exact rotation angles for the hour and minute hands and specify the count of 60 minute tick marks to eliminate geometric ambiguity. → Expected outcome: A watch with accurate time indication and a complete minute track.
- iter 3: Increase gear opacity to >= 0.8, correct second hand angle to 210°, and reinforce chain rendering. → Expected outcome: Visible movement gears, accurate second hand position, and a present chain.
- iter 4: Enforce sub-dial hand color to red or black to resolve the critique's concern about blue rendering. → Expected outcome: A watch with a sub-dial hand that strictly adheres to the red/dark color preference.
- iter 5: Replace the opaque dial with a semi-transparent lower half or clipped cutout to fully reveal the movement gears, and redraw the crown attachment as 3-4 distinct interlocking oval links. → Expected outcome: A watch with clearly visible gears beneath the dial and a physically accurate chain.