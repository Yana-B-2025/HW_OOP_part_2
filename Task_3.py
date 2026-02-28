# В папке лежит некоторое количество файлов. Считайте, что их 
# количество и имена вам заранее известны, пример для выполнения 
# домашней работы можно взять тут

# Необходимо объединить их в один по следующим правилам:

# Содержимое исходных файлов в результирующем файле должно 
# быть отсортировано по количеству строк в них (то есть первым 
# нужно записать файл с наименьшим количеством строк, а последним 
# - с наибольшим)
# Содержимое файла должно предваряться служебной информацией 
# на 2-х строках: имя файла и количество строк в нем


with open('1.txt', 'r', encoding='utf-8') as f1:
    file_1_lines = f1.readlines()
    quantity_of_lines_1 = len(file_1_lines)
    print(quantity_of_lines_1)

with open('2.txt', 'r', encoding='utf-8') as f2:
    file_2_lines = f2.readlines()
    quantity_of_lines_2 = len(file_2_lines)
    print(quantity_of_lines_2)

with open('3.txt', 'r', encoding='utf-8') as f3:
    file_3_lines = f3.readlines()
    quantity_of_lines_3 = len(file_3_lines)
    print(quantity_of_lines_3)

# Записm в один файл
with open('result.txt', 'w', encoding='utf-8') as res:
    res.write("2.txt\n")
    res.write(f"{quantity_of_lines_2}\n")
    res.writelines(file_2_lines)
    res.write("\n")
    res.write("1.txt\n")
    res.write(f"{quantity_of_lines_1}\n")
    res.writelines(file_1_lines) 
    res.write("\n")   
    res.write("3.txt\n")
    res.write(f"{quantity_of_lines_3}\n")
    res.writelines(file_3_lines)
    res.write("\n")

