import numpy as np

def backwardsCummulativeWeight(PSWM, theta, T, pi):
	lambdaMatrix = np.zeros(PSWM.shape)
	numberLetters, wordLength = PSWM.shape

	# initialize backward recursion
	for letter in range(numberLetters):
		wm_v = PSWM[letter, -1]
		lambda_m_v = np.exp(theta*wm_v)
		print
		lambdaMatrix[letter, -1] = lambda_m_v

	# perform backward recursion
	for locationInWord in range(wordLength-2, -1, -1):
		for letter in range(numberLetters):
			lambda_i_v  = 0			
			for nextLetter in range(numberLetters):
				sig_v_vp1 = T[letter, nextLetter]
				lambda_i_vp1 = lambdaMatrix[nextLetter, locationInWord+1]
				lambda_i_v += sig_v_vp1*lambda_i_vp1 
			wi_v = PSWM[letter, locationInWord]
			lambda_i_v *= np.exp(theta*wi_v)
			lambdaMatrix[letter, locationInWord] = lambda_i_v

	return lambdaMatrix

def computeWeightedNormalizationConst(lambdaMatrix):
	lambdaTheta = 0 # code here
	return lambdaTheta