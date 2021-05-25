import csv
import json

input_file_name = "./data/국민건강보험공단_건강검진정보_20191231.csv"
output_file_name = "./data/healthCheckup_20191231.json"
# input_file_name = "./data/국가_대륙_별_상품군별_온라인쇼핑_해외직접판매액_20210521181911.csv"
# output_file_name = "./data/k-beauty.json"

with open(input_file_name, "r", encoding="cp949", newline="") as input_file, \
        open(output_file_name, "w", encoding="UTF-8", newline="") as output_file:
    reader = csv.reader(input_file)

    # 첫 줄은 col_names 리스트로 읽어 놓고
    col_names = next(reader)

    # 그 다음 줄부터 zip으로 묶어서 json으로 dumps
    for cols in reader:
        doc = {col_name: col for col_name, col in zip(col_names, cols)}
        # print(json.dumps(doc, ensure_ascii=False, indent=4), file=output_file)
        json.dump(doc, output_file, indent=4, ensure_ascii=False)