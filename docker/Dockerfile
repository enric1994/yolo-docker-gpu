FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

RUN apt update -y && apt install -y \
python3 \
python3-pip \
git \
make \
libsm6 \
libxext6 \
libxrender-dev \
autoconf \
automake \
libtool \
build-essential \
libglib2.0-0

RUN cd /;git clone --recursive https://github.com/philipperemy/yolo-9000.git;cd yolo-9000;cat yolo9000-weights/x* > yolo9000-weights/yolo9000.weights

RUN sed -i s/GPU=0/GPU=1/g /yolo-9000/darknet/Makefile
RUN sed -i s/CUDNN=0/CUDNN=1/g /yolo-9000/darknet/Makefile

RUN cd /yolo-9000/darknet;make

RUN pip3 install \
opencv-python \
Flask \
scikit-image \
numpy \
matplotlib==2.1.0

