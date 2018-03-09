# cc-plugin-amf
AMF compliance checker plugin

The checks in this repo were generated automatically by `compliance-check-maker`.
They require my forked version of `compliance-check-lib` to run.

When generating new checks it would be painful to edit the `entry_points` list
in `setup.py` by hand - I use the following method

```
for f in cc_plugin_amf/amf_*.py; do
    check_name=`grep "name = " $f | tr -s " " | cut -d " " -f 4 | sed -e "s/'//g"`
    module_name=`basename $f | sed -e "s/.py//"`
    class_name=`grep class $f | cut -d ' ' -f 2 | cut -d '(' -f 1`

    echo "'$check_name = cc_plugin_amf.${module_name}:${class_name}',"
done
```

Note that this is probably very fragile and hacky...
