# These and other macros are documented in dhd/droid-hal-device.inc
%define device shieldtablet
%define vendor nvidia
%define vendor_pretty Nvidia
%define device_pretty Shield Tablet
%define installable_zip 1

%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc
