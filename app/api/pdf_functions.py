"""
    Generate PDF related functions
"""

def append_generated_html(html_file, insertion_point):
    # Read the content of the HTML file
    with open(html_file, 'r') as file:
        html_content = file.read()
        file.close()

    # Find the position to insert the div boxes
    insertion_index = html_content.find(insertion_point)
    if insertion_index == -1:
        print(f"Insertion point '{insertion_point}' not found in HTML file.")
        return

    # Define the div boxes to append
    div_boxes = '<div class="box"></div>\n<div class="box"></div>\n'

    # Insert the div boxes at the specified position
    updated_html_content = html_content[:insertion_index] + div_boxes + html_content[insertion_index:]

    # Write the updated content back to the HTML file
    return updated_html_content
    # with open(html_file, 'w') as file:
    #     file.write(updated_html_content)
