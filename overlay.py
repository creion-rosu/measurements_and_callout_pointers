import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_cad_overlay(text="12.5 mm", style='horizontal', filename='overlay.png'):
    """
    Generates a transparent CAD-style dimension overlay.
    
    Parameters:
    - text: The string to display in the box.
    - style: 'horizontal', 'vertical', or 'callout'.
    - filename: Output file path.
    """
    
    # ==========================================
    # PART 1: THE CONFIGURATION
    # ==========================================
    COLOR_CYAN  = '#00E5FF'  # The signature Cyan
    COLOR_TEXT  = '#1A222D'  # Dark (for inside the cyan box)
    FONT_FAMILY = 'IBM Plex Mono'
    FONT_SIZE   = 40
    LINE_WIDTH  = 2.5
    
    # ==========================================
    # PART 2: PLOTTING
    # ==========================================
    # Setup the figure (Transparent background)
    fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
    fig.patch.set_alpha(0.0) # Transparent figure
    ax.patch.set_alpha(0.0)  # Transparent axes
    ax.axis('off')           # No measurement axes
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)

    # ==========================================
    # PART 3: DRAWING LOGIC
    # ==========================================
    # Style A: Horizontal Measurement (<-- [ TEXT ] -->)
    if style == 'horizontal':
        # Draw the main line with arrows
        ax.annotate(
            '', xy=(1.6, 2.5), xytext=(2.6, 2.5),
            arrowprops=dict(arrowstyle='<|-|>', color=COLOR_CYAN, lw=LINE_WIDTH-0.5, mutation_scale=25)
        )
        # Draw the "End Caps" (Vertical lines at the measurement points)
        ax.plot([1.6, 1.6], [2.2, 2.8], color=COLOR_CYAN, lw=LINE_WIDTH) # Left Cap
        ax.plot([2.6, 2.6], [2.2, 2.8], color=COLOR_CYAN, lw=LINE_WIDTH) # Right Cap
        
        # Draw the Text Box in the center
        ax.text(
            6.0, 2.0, text,
            ha='center', va='center',
            color=COLOR_TEXT, fontsize=FONT_SIZE, weight='bold', family=FONT_FAMILY,
            bbox=dict(boxstyle="square,pad=0.2", fc=COLOR_CYAN, ec="none")
        )

    # Style B: Vertical Measurement (Up/Down Arrows)
    elif style == 'vertical':
        # We adjust limits for a taller aspect ratio feel
        ax.set_xlim(0, 5)
        ax.set_ylim(0, 10)
        
        # Main Line
        ax.annotate(
            '', xy=(2.5, 0.5), xytext=(2.5, 9.5),
            arrowprops=dict(arrowstyle='<|-|>', color=COLOR_CYAN, lw=LINE_WIDTH, mutation_scale=50)
        )
        # End Caps (Horizontal lines)
        ax.plot([2.2, 2.8], [0.5, 0.5], color=COLOR_CYAN, lw=LINE_WIDTH) # Bottom Cap
        ax.plot([2.2, 2.8], [9.5, 9.5], color=COLOR_CYAN, lw=LINE_WIDTH) # Top Cap
        
        # Text Box (Rotated 90 degrees or Horizontal? Usually horizontal is easier to read)
        #ax.text(
        #    2.5, 5.0, text,
        #    ha='center', va='center', rotation=90,
        #    color=COLOR_TEXT, fontsize=FONT_SIZE, weight='bold', family=FONT_FAMILY,
        #    bbox=dict(boxstyle="square,pad=0.6", fc=COLOR_CYAN, ec="none")
        #)

    # Style C: Callout Pointer (Line pointing to a spot)
    elif style == 'callout':
        # Point from (2,2) to (8,4)
        # The 'xy' is the target (the object), 'xytext' is where the label sits
        ax.annotate(
            text, 
            xy=(1.0, 1.0),      # The "Target" point (e.g., the LED filament)
            xytext=(6.0, 4.0),  # The "Label" location
            color=COLOR_TEXT, fontsize=FONT_SIZE, weight='bold', family=FONT_FAMILY,
            # Arrow properties
            arrowprops=dict(
                arrowstyle='->', 
                color=COLOR_CYAN, 
                lw=LINE_WIDTH, 
                connectionstyle="angle,angleA=0,angleB=90,rad=0" # Right-angle technical look
            ),
            # Box properties
            bbox=dict(boxstyle="square,pad=0.6", fc=COLOR_CYAN, ec="none")
        )
        
        # Add a small "Target Dot" at the tip
        circle = patches.Circle((1.0, 1.0), radius=0.1, color=COLOR_CYAN)
        ax.add_patch(circle)

    # 3. SAVE THE FILE
    # ------------------------------------------------
    plt.tight_layout()
    plt.savefig(filename, transparent=True, dpi=300)
    plt.close()
    print(f"Generated: {filename}")

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    # Generate 3 Standard Templates for your Library
    
    # 1. The "Width" Measure (Good for Battery size, Glue gap)
    create_cad_overlay("1.39V ↘ 1.27V", style='horizontal', filename='CAD_Overlay_Horizontal.png')
    
    # 2. The "Height" Measure (Good for Flame height, Stack size)
    create_cad_overlay("TEMP: 45C", style='vertical', filename='CAD_Overlay_Vertical.png')
    
    # 3. The "Spec" Callout (Good for pointing at LED filament or Crack)
    #create_cad_overlay("1800K CORE", style='callout', filename='CAD_Overlay_Callout.png')