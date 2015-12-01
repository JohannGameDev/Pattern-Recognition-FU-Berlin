close all;
clear all;
data = load('data/winequality-red.txt');

[a,b] = size(data);
needed_attribute = data(:,end);

max_cols = b-1;
hold on;
for i=1:max_cols
    subset_columns = combntns(1:max_cols,i);
    [sub_set_len, sub_set_width] = size(subset_columns);
    for j=1:sub_set_len
        cols = data(:,subset_columns(j,:));
        L = [ones(a,1), cols];
        % A = [b;m]
        A = needed_attribute * (L'*L)^(-1)*L';
        Y = L*A;
        E = sum((needed_attribute - Y).^2);
       	plot(sub_set_width, eval(sprintf('E%d%d',i,j)), '.k');
    end     
end
