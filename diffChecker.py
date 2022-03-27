import difflib

first_file = 'C:\\Users\\Asus\\workspace_python\\pythonBasics\\text_file_1.txt'
second_file = 'C:\\Users\\Asus\\workspace_python\\pythonBasics\\text_file_2.txt'

first_file_lines = open(first_file).readlines()
second_file_lines = open(second_file).readlines()

difference = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines, first_file, second_file)
difference_report = open('C:\\Users\\Asus\\workspace_python\\pythonBasics\\diff_files.html', 'w')
difference_report.write(difference)
difference_report.close()

