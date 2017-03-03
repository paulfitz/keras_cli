from __future__ import absolute_import
import argparse
import importlib


def keras_summary(filename, custom_objects):
    from keras.models import load_model
    model = load_model(filename, custom_objects=custom_objects)
    model.summary()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='model to use')
    parser.add_argument('--custom', action='append',
                        help='custom objects to load')
    args = parser.parse_args()
    custom_objects = {}
    if args.custom:
        for custom_file in args.custom:
            mod = importlib.import_module(custom_file)
            attrs = [(name, getattr(mod, name)) for name in dir(mod)
                     if not name.startswith('_')]
            custom_objects.update(attrs)
    keras_summary(args.filename, custom_objects)


if __name__ == '__main__':
    main()
