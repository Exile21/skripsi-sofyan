import csv

data = [
    {
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.004777799344526059,
    'averageMethane': 0.0001311462105199021,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.004777799344526059,
    'averageMethane': 0.0001311462105199021,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.004777799344526059,
    'averageMethane': 0.0001311462105199021,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.004777799344526059,
    'averageMethane': 0.0001311462105199021,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.004777799344526059,
    'averageMethane': 0.0001311462105199021,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.004777799344526059,
    'averageMethane': 0.0001311462105199021,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.0068287753574791015,
    'averageMethane': 0.00040385712969035696,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.006615306712486401,
    'averageCO': 0.004923718906007622,
    'averageMethane': 0.00013637065318656917,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.006615306712486401,
    'averageCO': 0.004923718906007622,
    'averageMethane': 0.00013637065318656917,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.006615306712486401,
    'averageCO': 0.004923718906007622,
    'averageMethane': 0.00013637065318656917,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.006615306712486401,
    'averageCO': 0.004923718906007622,
    'averageMethane': 0.00013637065318656917,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.006615306712486401,
    'averageCO': 0.00703244853341767,
    'averageMethane': 0.00014097474739975405,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.006705360063370518,
    'averageMethane': 0.0003999836236611292,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.004777799344526059,
    'averageMethane': 0.0001311462105199021,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.004777799344526059,
    'averageMethane': 0.0001311462105199021,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.004777799344526059,
    'averageMethane': 0.0001311462105199021,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.004777799344526059,
    'averageMethane': 0.0001311462105199021,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.004777799344526059,
    'averageMethane': 0.0001311462105199021,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.004777799344526059,
    'averageMethane': 0.0001311462105199021,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.005705547643392666,
    'averageMethane': 0.0001329715633124804,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.006705360063370518,
    'averageMethane': 0.00022287537501847524,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.0064148889735728245,
    'averageCO': 0.008418278494607669,
    'averageMethane': 0.00013976981220705452,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.00658504439978164,
    'averageMethane': 0.00016438763991275034,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.004635785291190435,
    'averageMethane': 0.00012610561604604637,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.004635785291190435,
    'averageMethane': 0.00012610561604604637,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.004635785291190435,
    'averageMethane': 0.00012610561604604637,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.004635785291190435,
    'averageMethane': 0.00012610561604604637,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.004635785291190435,
    'averageMethane': 0.00012610561604604637,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.004635785291190435,
    'averageMethane': 0.00012610561604604637,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.004635785291190435,
    'averageMethane': 0.00012610561604604637,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.013027912276985099,
    'averageMethane': 0.00015110862320814818,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 69.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.014977171385576304,
    'averageMethane': 0.0005729943881903598,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.020434596130316462,
    'averageCO': 0.00658504439978164,
    'averageMethane': 0.00016438763991275034,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.004635785291190435,
    'averageMethane': 0.00012610561604604637,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.004635785291190435,
    'averageMethane': 0.00012610561604604637,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.004635785291190435,
    'averageMethane': 0.00012610561604604637,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.004635785291190435,
    'averageMethane': 0.00012610561604604637,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.004635785291190435,
    'averageMethane': 0.00012610561604604637,
    },{
    'temperature': 29.0,
    'humidity': 68.0,
    'gasPercentage': 0.006219888761716435,
    'averageCO': 0.004635785291190435,
    'averageMethane': 0.00012610561604604637,
    }
]

with open('data_methane.csv', 'w', newline='') as csvfile:
    fieldnames = ['temperature', 'humidity', 'gasPercentage', 'averageCO', 'averageMethane', 'label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for sample in data:
        sample['label'] = 'normal'
        writer.writerow({'temperature': float(sample['temperature']), 'humidity': float(sample['humidity']), 'gasPercentage': float(sample['gasPercentage']), 'averageCO': float(sample['averageCO']), 'averageMethane': float(sample['averageMethane']), 'label': sample['label']})