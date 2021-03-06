__author__ = 'randxie'
#!/usr/bin/env python
from feature_manager import feature_manager
from multi_worker import multi_worker
from common_var import s_para, f_para
from support_fun import set_logging_config, output_feature1, output_feature2, clean_tmp_file

# set logging config
set_logging_config()

def main():
    # select operations
    tmp=raw_input('Select 1 or 2 to continue: \n'+
                  '[1] Generate feature 1 and 2 using single thread\n' +
                  '[2] Generate feature 1 and 2 using multiple thread (for large data size)\n'
                  '[3] Clear all data (DANGEROUS !!!!)\n'+
                  'P.S. I assume the new data will be appended into the end of tweets.txt. It will not take into account changes in previous tweets in tweets.txt\n')
    # for generating features
    if tmp=='1':
        f_manager=feature_manager(s_para)
        f_manager.calculate_feature(f_para)
        # output features
        output_feature1(f_manager.word_storage)
        output_feature2(f_manager.median_arr)
    elif tmp=='2':
        m_worker=multi_worker(s_para)
        m_worker.multi_calculate_feature(f_para)
        # output features
        output_feature1(m_worker.total_word_storage)
        output_feature2(m_worker.total_median_arr)
        # clean temporary file
        clean_tmp_file()
    # for delete all features
    elif tmp == '3':
        confirm =  raw_input('[WARNING] It will deleted all data. Are you sure that you want to continue(y/n)??')
        if confirm.lower() == 'y':
            f_manager=feature_manager(s_para)
            f_manager.__delete_all__()
            clean_tmp_file()
            print 'data are deleted'

if __name__ == "__main__":
    main()




