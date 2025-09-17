#F-String Alignment Example
#We can use <, >, and ^ inside f-strings to align text within a given width.
# Different alignment styles
print(f"{'Left':<10}|")     # < → Left aligned
print(f"{'Right':>10}|")    # > → Right aligned
print(f"{'Center':^10}|")   # ^ → Center aligned

'''
Output:
Left      |
     Right|
  Center  |
Explanation:
• <10 → text is placed on the left within 10 spaces.
• >10 → text is placed on the right within 10 spaces.
• ^10 → text is placed in the center within 10 spaces.
'''