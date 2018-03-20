import os
import sys

import argparse
import med2image.med2image as med2image

def convert(dicom_path, png_path):
	str_outputFileStem, str_outputFileExtension = os.path.splitext(png_path)
	
	if len(str_outputFileExtension):
		str_outputFileExtension = str_outputFileExtension.split('.')[1]
	try:
		str_inputFileStem, str_inputFileExtension = os.path.splitext(dicom_path)
	except:
		print(synopsis(False))
		sys.exit(1)

	args = {}
		
	args['outputFileType'] = str_outputFileExtension
	args['outputDir'] = '.'
	args['sliceToConvert'] = '-1'
	args['frameToConvert'] = '-1'
	args['showSlices'] = False
	args['reslice'] = False
	
	if len(str_outputFileExtension):
		args['outputFileStem'] = str_outputFileStem

	b_niftiExt = (str_inputFileExtension == '.nii' or
				  str_inputFileExtension == '.gz')
	b_dicomExt = str_inputFileExtension == '.dcm'
	if b_niftiExt:
		C_convert = med2image.med2image_nii(
			inputFile=dicom_path,
			outputDir=args['outputDir'],
			outputFileStem=args['outputFileStem'],
			outputFileType=args['outputFileType'],
			sliceToConvert=args['sliceToConvert'],
			frameToConvert=args['frameToConvert'],
			showSlices=args['showSlices'],
			reslice=args['reslice']
		)

		print('sliceToConvert:', args.sliceToConvert)

	if b_dicomExt:
		C_convert = med2image.med2image_dcm(
			inputFile=dicom_path,
			outputDir=args['outputDir'],
			outputFileStem=args['outputFileStem'],
			outputFileType=args['outputFileType'],
			sliceToConvert=args['sliceToConvert'],
			reslice=args['reslice']
		)

	# And now run it!
	med2image.misc.tic()
	C_convert.run()
	sys.exit(0)
	
if __name__ == '__main__':
	convert('000000.dcm', 'bleh.png')
