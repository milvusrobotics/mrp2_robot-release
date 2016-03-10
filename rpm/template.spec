Name:           ros-indigo-mrp2-robot
Version:        0.2.4
Release:        0%{?dist}
Summary:        ROS mrp2_robot package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/mrp2_robot
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-mrp2-bringup
Requires:       ros-indigo-mrp2-display
Requires:       ros-indigo-mrp2-hardware
BuildRequires:  ros-indigo-catkin

%description
MRP2 robot description and launch files

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Mar 10 2016 Akif Hacinecipoglu <akifhno@gmail.com> - 0.2.4-0
- Autogenerated by Bloom

* Tue Jan 12 2016 Akif Hacinecipoglu <akifhno@gmail.com> - 0.2.3-0
- Autogenerated by Bloom

* Tue Jan 12 2016 Akif Hacinecipoglu <akifhno@gmail.com> - 0.2.2-0
- Autogenerated by Bloom

* Tue Jan 12 2016 Akif Hacinecipoglu <akifhno@gmail.com> - 0.2.1-1
- Autogenerated by Bloom

