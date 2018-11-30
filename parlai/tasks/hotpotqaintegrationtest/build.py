import parlai.core.build_data as build_data
import os

def build(opt):
    # get path to data directory
    # TODO download path not fixed
    name = 'hotpot_train_v1.1'
    fname = name + '.json'
    dpath = os.path.join(opt['datapath'], name)
    # define version if any
    version = None

    # check if data had been previously built
    if not build_data.built(dpath, version_string=version):
        print('[building data: ' + dpath + ']')

        # make a clean directory if needed
        if build_data.built(dpath):
            # an older version exists, so remove these outdated files.
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # download the data.
        url = 'http://curtis.ml.cmu.edu/datasets/hotpot/' + fname # dataset URL
        build_data.download(url, dpath, fname)

        # mark the data as built
        build_data.mark_done(dpath, version_string=version)
