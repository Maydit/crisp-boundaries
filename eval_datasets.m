function [] = eval_datasets()
    folder = uigetdir;
    otherFolder = uigetdir;
    filePattern = fullfile(folder, '*.jpg');
    files = dir(filePattern);
    cd("Code")
    for k = 1 :length(files)
        baseFile = files(k).name;
        fullFile = fullfile(files(k).folder, baseFile);
        disp(fullFile);
        image = imread(fullFile);
        [E,~] = findBoundaries(image,'speedy');
        result = 1-mat2gray(E);
        newname = fullfile(otherFolder, baseFile);
        if exist(newname, 'file')
            delete(newname);
        end
        imwrite(result, newname, 'jpg');
    end
end
