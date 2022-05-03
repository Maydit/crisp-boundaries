function [] = eval_datasets()
    cd('Code')
    folder = '..\datasets\t';
    otherFolder = '..\datasets\e';
    filePattern = fullfile(folder, '*.png');
    files = dir(filePattern);
    for k = 1:length(files)
        baseFile = files(k).name;
        fullFile = fullfile(files(k).folder, baseFile);
        image = imread(fullFile);
        [E,E_oriented] = findBoundaries(image,'speedy');
        result = 1-mat2gray(E);
        imwrite(result, fullfile(otherFolder, baseFile));
    end
end
