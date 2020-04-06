import read_file
import  analyze
import mobile_email


text  = read_file.read_file('test_resumes/pdf/6.pdf')
output = analyze.extract_data(text)
mob,em = mobile_email.get_mobile_email(text)

print(f'Mobile No\t:{mob}\nEmail Id\t:{em}')
for i in output:
    if i not in ('location','timeperiod'):
        print(i,'\t:',output[i])