################## 학습데이터처리 시간입니다 ##################
################## ai 기초 프로그래밍 마저 마무리 ##################
################## Report 있음 ######################

import os
import glob
import json
# from pprint import pp # 이쁘게 프린트 합시다.

# 1. glob을 이용하여 폴더 내에 모든 json파일 read
files = glob.glob("C:/Users/AI-00/Desktop/lecture/CAM_FRONT/*.json")
# print(files) # ['C:/Users/AI-00/Desktop/lecture/CAM_FRONT\\000000.json', 'C:/Users/AI-00/Desktop/lecture/CAM_FRONT\\000001.json', 'C:/Users/AI-00/Desktop/lecture/CAM_FRONT\\000002.json', 'C:/Users/AI-00/Desktop/lecture/CAM_FRONT\\000003.json', 'C:/Users/AI-00/Desktop/lecture/CAM_FRONT\\000004.json', 'C:/Users/AI-00/Desktop/lecture/CAM_FRONT\\000005.json', 'C:/Users/AI-00/Desktop/lecture/CAM_FRONT\\000006.json', 'C:/Users/AI-00/Desktop/lecture/CAM_FRONT\\000007.json', 'C:/Users/AI-00/Desktop/lecture/CAM_FRONT\\000008.json', 'C:/Users/AI-00/Desktop/lecture/CAM_FRONT\\000009.json', 'C:/Users/AI-00/Desktop/lecture/CAM_FRONT\\modified_000000.json']

# 1-1. os 이용해서 파일명만 저장해보도록 합시다.
for file in files:
    jsonfile = os.path.basename(file)
    filename = jsonfile.split(".")[0]

    # 2. open, json.load()를 통해 json파일 load
    f = open(file)
    json_data = json.load(f)

    # 2. level 0 이 아닌 것, 클래스가 Dontcare인 거 삭제하고 새로운 new_object 리스트에 넣어준다.
    new_object = []
    for i, classes in enumerate(json_data["Object"]):
        if classes["level"] == 0 and classes["class"] != "Dontcare":
            new_object.append(classes)

    # 3. Truck, Car는 Vehicle로 통일
    for i, classes in enumerate(new_object):
        if classes["class"] == "Truck" or classes["class"] == "Car":
            classes["class"] = "Vehicle"

    # 2, 3 이 잘되었는지 확인해봅시다.
    # for i, classes in enumerate(new_object):
    #     print(i, classes)

    # 4. json_data["Object"]를 전처리한 new_object 리스트로 대체!
    print(new_object)
    json_data["Object"] = new_object
    print(json_data)

    f.close()

    # 5. 저장합시다.
    f = open("C:/Users/AI-00/Desktop/lecture/CAM_FRONT/modified_" + filename + ".json", "w")
    json.dump(json_data, f, indent="\t")
    f.close()