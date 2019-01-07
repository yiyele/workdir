# -*- coding: utf-8 -*-
#/usr/bin/python2

"""
File Name: tfprof
Auther: xxq
Date: 19-1-2
Describes:
    - tools for tensorflow
    - tfprof : import model and analysis model
    - tools : load model / print train variables / print float point / print memory usage / read tfrecord file
"""
import tensorflow as tf
from tensorflow.contrib.tfprof import model_analyzer
from tensorflow.python.tools import inspect_checkpoint


def load_model(sess, ckpt_path):
    ckpt = tf.train.get_checkpoint_state(ckpt_path)
    if ckpt and ckpt.model_checkpoint_path:
        tf.logging.info(ckpt.model_checkpoint_path)
        tf.logging.info('{}.meta'.format(ckpt.model_checkpoint_path))
        saver = tf.train.import_meta_graph('{}.meta'.format(ckpt.model_checkpoint_path))
        saver.restore(sess, ckpt.model_checkpoint_path)


# print train variables
def print_train_variables():
    model_analyzer.print_model_analysis(graph,tfprof_options=model_analyzer.TRAINABLE_VARS_PARAMS_STAT_OPTIONS)


# print floating poing operations
def print_floating_point_operations():
    model_analyzer.print_model_analysis(graph, tfprof_options=model_analyzer.FLOAT_OPS_OPTIONS)


# print memory usage
def print_memory_usage(run_metadata):
    model_analyzer.print_model_analysis(graph, run_meta=run_metadata,
                                        tfprof_options=model_analyzer.FLOAT_OPS_OPTIONS)

# read tfrecord file
def read_tfrecord():
    for example in tf.python_io.tf_record_iterator("../model/output_xiaoai_classes7/train.tf_record"):
        result = tf.train.Example.FromString(example)
        tf.logging.info(result)


if __name__ == "__main__":
    tf.logging.set_verbosity(tf.logging.INFO)
    ckpt_path = '../model/baseline_gru'
    graph = tf.get_default_graph()
    read_tfrecord()
    with tf.Session(graph=graph) as sess:
        #inspect_checkpoint.print_tensors_in_checkpoint_file(file_name='/home/yiyele/PycharmProjects/projects/tf_tools/model/test/model.ckpt-200000',
        #                                                   tensor_name='', all_tensors=True, all_tensor_names=True)
        load_model(sess, ckpt_path)
        options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
        run_metadata = tf.RunMetadata()
        # sess.run(options=options, run_metadata=run_metadata)
        print_train_variables()
        print_floating_point_operations()
        print_memory_usage(run_metadata)
