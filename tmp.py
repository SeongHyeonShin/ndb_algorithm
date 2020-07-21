# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:50:29 2018

@author: SHIN

MID BAND : SR
HIGH BAND : AE

0503 수정 : 0_12kHz까지 학습한 NN출력 사용!
0524 수정 : sign VQ 적용
0529 수정 : max 값에 대한 새로운 정의
0606 수정 : sign 전송 방법 switching 구조
0608 수정 : high band 전송 switching 구조
0616 수정 : even frame 조절
0624 수정 : mid band AE 대입

"""

import numpy as np
import mdct
from scipy import signal
import struct as st
import csv
import highband_restore as hr
import reconstruction_model as rm


def read_result(filename, dim, datatype='float64'):
    """
    "   para : filename
    "   para : dim      : feature dimension
    """
    fin = open(filename, "rb")
    result = fin.read(-1)
    result = np.fromstring(result, datatype)

    fin.close()

    """
    "   reshape (#ofdata, feature)
    """
    if dim != 1:
        result = np.reshape(result, (-1, dim))

    return result


def sgn(num):
    if num > 0:
        return 1.0
    elif num < 0:
        return -1.0
    else:
        return 0.


def randsgn():
    sum_sign = np.random.randint(-10, 10)
    if sum_sign >= 0:
        return 1
    else:
        return -1


def cal_MDCT(tmp_file, window_size):
    #
    #
    #
    window = signal.cosine(window_size)
    half_size = window_size // 2
    fin = open("./TEST_DB_copy/%d.wav" % tmp_file, "rb")

    ori = fin.read(-1)
    ori = np.fromstring(ori, 'short')
    ori = ori[22:]

    fin.close()

    zero = np.zeros(half_size)
    ori = np.append(zero, ori)

    spec = np.zeros((len(ori) // half_size - 1, half_size))
    for i in range(len(ori) // half_size - 1):
        data = ori[half_size * i:half_size * i + window_size] * window
        spec[i] = mdct.fast.transforms.mdct(data)

    return spec


def mdct_to_wave(data, labels, original, test_high, band_ssh, out_filename):
    """
    "   para : data  : output data (#ofdata, output dimension = 768)
    "          gain  : global gain (#ofdata, band_size = 1)
    "          labels: input data  (#ofdata, input dimension = 1024)
    """
    band_size = 768
    highband_size = 128
    window_size = 2048
    answer = 128
    highband_threshold = 1500

    half_window = int(window_size / 2)
    window = signal.cosine(window_size)

    pre_wave = np.zeros(half_window)
    result = np.zeros(half_window)

    fout = open(out_filename, "wb")

    labels /= 45.25
    labels = labels[1:]
    labels_high = np.split(labels, [band_size, band_size + highband_size], 1)[1]
    # labels = np.split(labels, [band_size], 1)[0]

    """
    band :
        1. 4 (256) ~ 6 (384)
        2. 6 (384) ~ 9 (576)
        3. 9 (576) ~ 12(768) 

        [132, 144, 160, 176, 196, 216, 240, 264, 292, 320, 352, 384, 416, 448, 480, 512, 544, 576, 608]

        6  : [15.36   33.78   27.84]   [22.96   24.82   13.00]
        10 : [12.79   31.95   27.53]   [18.07   23.23   12.77]
        13 : [16.90   40.92   31.48]   [22.83   29.18   15.74]
        14 : [16.50   31.13   31.56]   [20.39   25.04   18.72]
        16 : [14.44   31.89   31.76]   [18.73   24.64   17.42]
        27 : [11.14   26.01   30.83]   [12.39   22.78   18.99]
        29 : [12.93   28.51   31.66]   [14.20   23.79   19.77]
        32 : [16.79   38.22   34.33]   [21.88   28.84   17.00]
        35 : [13.83   35.46   31.26]   [17.04   25.10   14.30]
        36 : [15.44   31.95   25.14]   [19.74   23.81   12.63]
        40 : [15.47   37.93   32.13]   [18.15   26.44   14.33]
        42 : [9.48    27.11   25.71]   [14.03   20.63   13.08]   
    """
    band = [264, 292, 320, 352, 384, 416, 448, 480, 512, 544, 576, 608, 640, 672, 704, 736, 768]
    band = np.asarray(band) // 2 - 128
    ae_band = [24, 24, 24, 24, 32, 32, 32, 32, 32]

    pre_frame = np.zeros(band_size + 1)
    band_energy_odd = np.zeros((len(data) // 2, 9))
    band_energy_even = np.zeros((len(data) // 2, 9))

    band_count = np.zeros((len(data), 10))

    p_or_m = np.zeros((len(data), 2))
    error_ori = np.zeros((len(data), 256))
    sign_idx = 256
    zero_threshold = 10
    _iter = np.min([len(data), len(original), len(labels)]

                   for i in range(0, _iter, 2):
    # 1 - frame
    # Odd

    """
    "   Data setting
    """

    spec = original[i]
    spec_data = [spec[j] for j in range(len(labels[i])) if j % 2 == 1]

    odd_data = np.asarray([data[i][j] for j in range(len(data[i])) if j % 2 == 1]) * np.sign(spec_data[128:])
    labels_even = np.asarray([labels[i][j] for j in range(len(labels[i])) if j % 2 == 0])

    n_labels_even = labels_even.copy()
    n_labels_even /= np.sum(np.abs(n_labels_even))

    band_energy_even[i // 2] = rm.cal_band_energy(n_labels_even[answer:])
    band_count_extention = np.zeros(256)

    for j in range(len(band_energy_even[i // 2])):
        if
    band_energy_even[i // 2][j] < 2.e-4:
    band_count[i][j + 1] += 1
    band_count_extention[int(np.sum(ae_band[:j])):int(np.sum(ae_band[:j + 1]))] = 1

    if np.sum(band_count[i][6:]) > 2:
        zero_threshold = 3
    sign_idx = 128
    else:
    zero_threshold = 4
    sign_idx = 255

    """
    "   Gain
    """
    for j in range(len(band_ssh)):
        pre_idx = int(np.sum(band_ssh[:j]))
    post_idx = int(np.sum(band_ssh[:j + 1]))

    gain = np.mean(np.abs(labels_even[answer + pre_idx:answer + post_idx]))
    odd_gain = np.mean(np.abs(odd_data[pre_idx:post_idx]))

    if odd_gain != 0:
        odd_data[pre_idx:post_idx] = odd_data[pre_idx:post_idx] * gain / odd_gain
    else:
        odd_data[pre_idx:post_idx] = odd_data[pre_idx:post_idx] * 0

    output_data = np.zeros(len(labels_even))
    output_data[answer:] = odd_data

    """
    "   Extra data
    """
    extra_idx = []
    for j in range(sign_idx):
        zero_count = 0

    if labels[i][2 * j + answer * 2] == 0.:
        zero_count += 1
    if labels[i][2 * (j + 1) + answer * 2] == 0.:
        zero_count += 1
    if pre_frame[2 * j + 1 + answer * 2] == 0.:
        zero_count += 1
    if labels[i + 1][2 * j + 1 + answer * 2] == 0.:
        zero_count += 1

    if zero_count >= zero_threshold:
    # idx 저장
        extra_idx.append(j)

    for j in range(len(extra_idx)):
        idx = int(extra_idx[j])
    output_data[answer + idx] = labels[i][2 * answer + 2 * idx + 1]

    # count = 0
    # for j in range(len(output_data[answer:])):
    #     if sgn(output_data[answer + j]) != sgn(spec_data[answer + j]):
    #         count += 1
    #         error_ori[j] += 1

    # output = [labels[i][j] if j % 2 == 0 else sgn(spec_data[j // 2]) * np.abs(output_data[j // 2]) for j in range(len(labels[i]))]
    output = [labels[i][j] if j % 2 == 0 else output_data[j // 2] for j in range(len(labels[i]))]
    output = np.asarray(output)

    """
    "   Highband data
    """
    if np.max(np.abs(labels_high[i])) + np.max(np.abs(labels_high[i + 1])) > highband_threshold:
        test_high[i] = labels_high[i]
    band_count[i][0] = 1
    else:
    sign_high = hr.harmonic_filter(output, test_high[i], 128, 32, band_size)

    for p in range(highband_size):
        if
    sign_high[p] != 0:
    test_high[i][p] = test_high[i][p] * sgn(sign_high[p])
    else:
    test_high[i][p] = test_high[i][p] * randsgn()

    result[:band_size] = output
    result[:2 * answer] = labels[i][:2 * answer]
    result[band_size:band_size + highband_size] = test_high[i]

    output = mdct.fast.transforms.imdct(result)
    output *= window

    wave = pre_wave + output[:half_window]
    pre_wave = output[half_window:]

    for j in range(len(wave)):
        if
    wave[j] > 32767:
    wave[j] = 32767
    elif wave[j] < -32767:
    wave[j] = -32767

    for j in range(len(wave)):
        fout.write(st.pack('h', int(wave[j] + 0.5)))

    frame1.append(count)

    #######################################################################################################

    # 2 - frame
    # Even

    """
    "   data setting
    """
    spec = original[i + 1]
    spec_data = [spec[j] for j in range(len(labels[i + 1])) if j % 2 == 0]

    even_data = np.asarray([data[i + 1][j] for j in range(len(data[i + 1])) if j % 2 == 0]) * np.sign(spec_data[128:])
    labels_odd = np.asarray([labels[i + 1][j] for j in range(len(labels[i + 1])) if j % 2 == 1])

    n_labels_odd = labels_odd.copy()
    n_labels_odd /= np.sum(np.abs(n_labels_odd))

    band_energy_odd[i // 2] = rm.cal_band_energy(n_labels_odd[answer:])
    band_count_extention = np.zeros(256)

    for j in range(len(band_energy_odd[i // 2])):
        if
    band_energy_odd[i // 2][j] < 2.e-4:
    band_count[i + 1][j + 1] += 1
    band_count_extention[int(np.sum(ae_band[:j])):int(np.sum(ae_band[:j + 1]))] = 1

    if np.sum(band_count[i + 1][6:]) > 2:
        zero_threshold = 3
    sign_idx = 128
    else:
    zero_threshold = 4
    sign_idx = 256

    """
    "   Gain
    """
    for j in range(len(band_ssh)):
        pre_idx = int(np.sum(band_ssh[:j]))
    post_idx = int(np.sum(band_ssh[:j + 1]))

    gain = np.mean(np.abs(labels_odd[answer + pre_idx:answer + post_idx]))
    even_gain = np.mean(np.abs(even_data[pre_idx:post_idx]))

    if even_gain != 0:
        even_data[pre_idx:post_idx] = even_data[pre_idx:post_idx] * gain / even_gain
    else:
        even_data[pre_idx:post_idx] = even_data[pre_idx:post_idx] * 0

    output_data = np.zeros(band_size // 2)
    output_data[answer:] = even_data

    """
    "   Extra data
    """
    extra_idx = []
    for j in range(sign_idx):
        zero_count = 0

    if labels[i + 1][2 * j - 1 + answer * 2] == 0.:
        zero_count += 1
    if labels[i + 1][2 * j + 1 + answer * 2] == 0.:
        zero_count += 1
    if labels[i][2 * j + answer * 2] == 0.:
        zero_count += 1

    if zero_count >= zero_threshold - 1:
    # idx 저장
        extra_idx.append(j)

    # for j in range(256):
    #     if band_count_extention[j] != 0:
    #         output_data[answer + j] = randsgn() * output_data[answer + j]

    for j in range(len(extra_idx)):
        idx = int(extra_idx[j])
    output_data[answer + idx] = labels[i + 1][2 * answer + 2 * idx]

    lengthofextra.append((len(extra_idx)))

    # count = 0
    # for j in range(len(output_data[answer:])):
    #     if sgn(output_data[answer + j]) != sgn(spec_data[answer + j]):
    #         count += 1
    #         error_ori[j] += 1

    #     error.append(np.abs(spec_data[answer + j]) - np.abs(output_data[answer + j]))

    # output = [labels[i + 1][j] if j % 2 == 1 else sgn(spec_data[j // 2]) * np.abs(output_data[j // 2]) for j in range(len(labels[i + 1]))]
    output = np.asarray([labels[i + 1][j] if j % 2 == 1 else output_data[j // 2] for j in range(len(labels[i + 1]))])

    """
    "   Highband data
    """

    if np.max(np.abs(labels_high[i])) + np.max(np.abs(labels_high[i + 1])) > highband_threshold:
        test_high[i + 1] = labels_high[i + 1]
    band_count[i + 1][0] = 1
    else:
    sign_high = hr.harmonic_filter(output, test_high[i + 1], 128, 32, band_size)

    for p in range(highband_size):
        if
    sign_high[p] != 0:
    test_high[i + 1][p] = test_high[i + 1][p] * sgn(sign_high[p])
    else:
    test_high[i + 1][p] = test_high[i + 1][p] * randsgn()

    result[:band_size] = output
    result[:2 * answer] = labels[i + 1][:2 * answer]
    result[band_size:band_size + highband_size] = test_high[i + 1]

    output = mdct.fast.transforms.imdct(result)
    output *= window

    pre_frame = labels[i + 1]
    wave = pre_wave + output[:half_window]
    pre_wave = output[half_window:]

    for j in range(len(wave)):
        if
    wave[j] > 32767:
    wave[j] = 32767
    elif wave[j] < -32767:
    wave[j] = -32767

    for j in range(len(wave)):
        fout.write(st.pack('h', int(wave[j] + 0.5)))

    frame2.append(count)

    fout.close()

    return p_or_m, error_ori, band_count


if __name__ == "__main__":
    tmp_file_list = [6]  # , 10, 13, 14, 16, 27, 29, 32, 35, 36, 40, 42]
    band_idx = [24, 24, 24, 24, 32, 32, 32, 32, 32]
    f = open("./TOTALBAND_RESULT/error_ratio_Q_O.csv", "w", newline='')
    csv_writer = csv.writer(f)

    for idx in range(len(tmp_file_list)):
        tmp_file = tmp_file_list[idx]

        test_data = read_result("./CNN_OUTPUT/NEW_MODEL/%d_requant_result.raw" % tmp_file,
                                512, datatype='float32')
        test_labels = read_result("./2048_MDCT_48kbps_UNET_32K/relu_file_12kHz/%d_requant_out.raw" % tmp_file,
                                  1024)

        origianl = cal_MDCT(tmp_file, 2048)
        tmp_ori = origianl.copy()
        test_highband, _ = hr.highband_quantizer(tmp_ori, test_labels)
        test_highband *= 0.7
        # test_highband = []
        pm, eo, bc = mdct_to_wave(test_data,
                                  test_labels,
                                  origianl,
                                  test_highband,
                                  band_idx,
                                  "./TOTALBAND_RESULT/FD_NEW_%d.raw" % tmp_file)
        """
        fout = open("./TOTALBAND_RESULT/zero/%d_new.raw" % tmp_file, "wb")
        for j in range(len(bc)):
            for jj in range(10):
                fout.write(st.pack('h', int(bc[j][jj] + 0.5)))
        fout.close()

        tmp_bc = bc.sum(axis=0)
        """
        for j in range(len(eo)):
            csv_writer.writerow(eo[j])
        csv_writer.writerow('')
        print()
        print("[%d 완료]" % idx)

    f.close()

