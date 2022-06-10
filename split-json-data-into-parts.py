import json

# add your file path here
file_path = '/Users/vibinkishore/.../final_export.json'

with open(file_path, 'r') as f1:
    ll = json.loads(f1.read())
    print('File has {} records'.format(len(ll)))

    #add the split range here
    size_of_the_split=100

    total = len(ll) // size_of_the_split
    print('Number of files to be exported are {}'.format(total+1))
    for i in range(total+1):

        #add the export folder path
        export_path = '/Users/vibinkishore/.../split_files_new'

        json.dump(ll[i * size_of_the_split:(i + 1) * size_of_the_split], open(export_path + '/export_file_' + str(i+1) + ".json", 'w',
            encoding='utf8'), ensure_ascii=False, indent=4)
            
    print('File split done')
