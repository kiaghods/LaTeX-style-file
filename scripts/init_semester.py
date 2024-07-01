import os
import shutil
import yaml

def create_directory(path):
    """Creates a directory if it doesn't already exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def copy_file(src, dest):
    """Copies a file from src to dest."""
    if os.path.exists(src):
        shutil.copy(src, dest)
    else:
        print(f"Source file {src} does not exist.")

def create_file(path, content=''):
    """Creates a file with the given content."""
    with open(path, 'w') as f:
        f.write(content)

def create_info_yaml(course_path, course_info):
    """Creates an info.yaml file with course information."""
    info_path = os.path.join(course_path, 'info.yaml')
    with open(info_path, 'w') as f:
        yaml.dump(course_info, f)

def format_directory_name(name):
    """Formats a name to lowercase with underscores."""
    return name.lower().replace(' ', '_')

def initialize_course_structure(course_path, is_self_study, num_problem_sets=0):
    """Initializes the directory structure for a course."""
    tex_path = os.path.join(course_path, 'tex')
    pdf_path = os.path.join(course_path, 'pdf')
    create_directory(tex_path)
    create_directory(pdf_path)

    topic_name = os.path.basename(course_path)
    if is_self_study:
        create_file(os.path.join(tex_path, 'notes.tex'))
        create_file(os.path.join(tex_path, 'solutions.tex'))
        create_file(os.path.join(tex_path, 'compile_notes_and_solutions.tex'))
        create_file(os.path.join(tex_path, 'compile_notes_only.tex'))
        create_file(os.path.join(tex_path, 'compile_solutions_only.tex'))
        create_file(os.path.join(pdf_path, f'{topic_name}_notes.pdf'))
        create_file(os.path.join(pdf_path, f'{topic_name}_solutions.pdf'))
        create_file(os.path.join(pdf_path, f'{topic_name}_notes_and_solutions.pdf'))
    else:
        create_directory(os.path.join(tex_path, 'notes'))
        create_directory(os.path.join(tex_path, 'problem_sets'))
        create_file(os.path.join(tex_path, 'notes', f'master_notes_{topic_name}.tex'))
        for i in range(1, num_problem_sets + 1):
            create_file(os.path.join(tex_path, 'problem_sets', f'ProblemSet{i}_{topic_name}_kg.tex'))
            create_file(os.path.join(pdf_path, f'ProblemSet{i}_{topic_name}_kg.pdf'))
        create_file(os.path.join(pdf_path, f'{topic_name}_notes_kg.pdf'))

def initialize_semester():
    """Initializes a semester directory and its courses."""
    semester = input("What time period are you setting up (e.g., summer_2024): ").strip()
    create_directory(semester)
    create_file(os.path.join(semester, 'kia.sty'))  # Create an empty kia.sty file

    num_topics = int(input("How many topics are you studying: "))
    for i in range(1, num_topics + 1):
        print(f"\nThe following info is for Topic {i}:\n")
        course_type = input("Is this a self study or a course (self-study/course): ").strip().lower()
        if course_type == 'self-study':
            topic = input("Topic: ").strip()
            textbook = input("Textbook (optional): ").strip()
            url = input("Equivalent Princeton course URL (if applicable, leave blank if not): ").strip()
            course_info = {
                'type': 'self-study',
                'topic': topic,
                'textbook': textbook if textbook else None,
                'url': url if url else None
            }
            course_path = os.path.join(semester, 'self-study', format_directory_name(topic))
        else:
            title = input("Title: ").strip()
            course_code = input("Course Code: ").strip()
            textbook = input("Textbook (optional): ").strip()
            url = input("URL (optional): ").strip()
            num_problem_sets = int(input(f"How many problem sets for {course_code}: ").strip())
            course_info = {
                'type': 'course',
                'title': title,
                'course_code': course_code,
                'textbook': textbook if textbook else None,
                'url': url if url else None,
                'num_problem_sets': num_problem_sets
            }
            course_path = os.path.join(semester, format_directory_name(course_code))
        
        create_directory(course_path)
        create_info_yaml(course_path, course_info)
        initialize_course_structure(course_path, course_type == 'self-study', num_problem_sets if course_type != 'self-study' else 0)

if __name__ == '__main__':
    initialize_semester()
    print("Semester initialized.")