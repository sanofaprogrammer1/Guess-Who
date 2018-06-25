import numpy as np
import random
from gym.envs.guesswho.player import Player
from gym.envs.guesswho.gameboard import gameBoard
from gym.envs.guesswho.agent import Agent

class Game:

	p1 = None
	p2 = None
	numTurns = 0
	status = ''
	numFlipped = 0

	def __init__(self):
		sel = np.random.randint(0, 24)
		g1 = gameBoard(sel)
		self.p1 = Player("PLAYER 1", g1, sel)
		#self.p1 = Agent("Charlie", g1, sel)
		print(self.p1.getName() + " selected " + self.p1.getBoard().getCharacter(self.p1.getBoard().getSelected()).getName())
		j = np.random.randint(0, 24)
		g2 = gameBoard(j)
		#self.p2 = Player("PLAYER 2", g2, j)
		self.p2 = Agent("Alex", g2, j)
		print(self.p2.getName() + " selected " + self.p2.getBoard().getCharacter(self.p2.getBoard().getSelected()).getName())
		self.status = 'START'
		self.numFlipped = 0
		self.numTurns = 0
		self.gameOver = False
		#isFemale to hasButtchin + the five hair colors + m + n 
		self.selTraits = np.zeros(20)

	def updateSelTraits(self, i, correct):
		if correct is False:
			self.selTraits[i] = -1
		else:
			self.selTraits[i] = 1

	# Resets game 
	def resetBoard(self):
		i = np.random.randint(0, 24)
		j = np.random.randint(0, 24)
		self.p1.selectedCharacter = i
		self.p2.selectedCharacter = j
		g1 = gameBoard(i)
		g2 = gameBoard(j)
		self.p1.setBoard(g1)
		self.p2.setBoard(g2)
		self.numTurns = 0
		self.status = 'START'
		self.numFlipped = 0
		self.gameOver = False
		self.selTraits = np.zeros(20)
		print("RESET BOARD")


	def step(self): #returns status 
		if(self.status == 'WON' or self.status == 'LOST'):
			return self.status
		else:
			print("STATE NUMFLIPPED " + str(self.numFlipped))
			return str(self.numFlipped)

	def getState(self):
		self.selTraits[18] = self.p1.getBoard().numberActive()
		self.selTraits[19] = self.p2.getBoard().numberActive()
		return self.selTraits

	def getAction(self, i, pturn):
		if pturn:
			player = self.p1
			otherplayer = self.p2
		else:
			player = self.p2
			otherplayer = self.p1
		#each number corresponds to an action 
		#auto quit (debug only)
		if i == -1:
			quit()
		#guess specific character
		elif i >= 0 and i < 24:
			if(i == otherplayer.getBoard().getSelected()):
				print("CORRECT GUESS")
				player.setScore(player.getScore() + 1)
				if pturn:
					self.status = 'WON'
				else:
					self.status = 'LOST'
			else:
				print("INCORRECT GUESS")
				otherplayer.setScore(otherplayer.getScore() + 1)
				if pturn:
					self.status = 'LOST'
				else:
					self.status = 'WON'
			return 
		#y/n questions
		elif i == 24:
			characterList, numFlipped = player.getBoard().askQ('isFemale', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
			if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('isFemale'):
				self.updateSelTraits(0, True)
			elif pturn:
				self.updateSelTraits(0, False)
		elif i == 25:
			characterList, numFlipped = player.getBoard().askQ('hasHat', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
			if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasHat'):
				self.updateSelTraits(1, True)
			elif pturn:
				self.updateSelTraits(1, False)
		elif i == 26:
			characterList, numFlipped = player.getBoard().askQ('hasGlasses', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
			if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasGlasses'):
				self.updateSelTraits(2, True)
			elif pturn:
				self.updateSelTraits(2, False)
		elif i == 27:
			characterList, numFlipped = player.getBoard().askQ('hasBeard', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
			if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasBeard'):
				self.updateSelTraits(3, True)
			elif pturn:
				self.updateSelTraits(3, False)
		elif i == 28:
			characterList, numFlipped = player.getBoard().askQ('hasMustache', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
			if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasMustache'):
				self.updateSelTraits(4, True)
			elif pturn:
				self.updateSelTraits(4, False)
		elif i == 29:
			characterList, numFlipped = player.getBoard().askQ('hasRosyCheeks', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
			if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasRosyCheeks'):
				self.updateSelTraits(5, True)
			elif pturn:
				self.updateSelTraits(5, False)
		elif i == 30:
			characterList, numFlipped = player.getBoard().askQ('isSmiling', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
			if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('isSmiling'):
				self.updateSelTraits(6, True)
			elif pturn:
				self.updateSelTraits(6, False)
		elif i == 31:
			characterList, numFlipped = player.getBoard().askQ('isBald', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
			if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('isBald'):
				self.updateSelTraits(7, True)
			elif pturn:
				self.updateSelTraits(7, False)
		elif i == 32:
			characterList, numFlipped = player.getBoard().askQ('hasBlueEyes', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
			if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasBlueEyes'):
				self.updateSelTraits(8, True)
			elif pturn:
				self.updateSelTraits(8, False)
		elif i == 33:
			characterList, numFlipped = player.getBoard().askQ('hasBigNose', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
			if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasBigNose'):
				self.updateSelTraits(9, True)
			elif pturn:
				self.updateSelTraits(9, False)
		elif i == 34:
			characterList, numFlipped = player.getBoard().askQ('hasBigMouth', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
			if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasBigMouth'):
				self.updateSelTraits(10, True)
			elif pturn:
				self.updateSelTraits(10, False)
		elif i == 35:
			characterList, numFlipped = player.getBoard().askQ('hasEarrings', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
			if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasEarrings'):
				self.updateSelTraits(11, True)
			elif pturn:
				self.updateSelTraits(11, False)
		elif i == 36:
			characterList, numFlipped = player.getBoard().askQ('hasButtchin', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
			if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasButtchin'):
				self.updateSelTraits(12, True)
			elif pturn:
				self.updateSelTraits(12, False)
		#binary search
		elif i == 37:
			binaryPositions, characterlist, numFlipped = player.getBoard().binarySearch(player.getBinaryPositions(), otherplayer.getBoard())
			player.getBoard().updateList(characterlist)
			player.setBinaryPositions(binaryPositions)
		#hair colors
		else:
			characterlist, numFlipped = player.getBoard().askHairColor(i, otherplayer.getBoard())
			player.getBoard().updateList(characterlist)
			if i == 38:
				if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('black'):
					self.updateSelTraits(13, True)
				elif pturn:
					self.updateSelTraits(13, False)
			if i == 39:
				if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('red'):
					self.updateSelTraits(14, True)
				elif pturn:
					self.updateSelTraits(14, False)
			if i == 40:
				if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('white'):
					self.updateSelTraits(15, True)
				elif pturn:
					self.updateSelTraits(15, False)
			if i == 41:
				if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('blonde'):
					self.updateSelTraits(16, True)
				elif pturn:
					self.updateSelTraits(16, False)
			else:
				if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('brown'):
					self.updateSelTraits(17, True)
				elif pturn:
					self.updateSelTraits(17, False)
		if pturn:
			self.p1 = player
			self.numFlipped = numFlipped
			print("NUMFLIPPED : " + str(self.numFlipped))
			self.state = self.numFlipped
		else:
			self.p2 = player

	def oneTurn(self, action): 
		#the bot/player goes 
		print(self.p1.getName() + " is guessing" + str(action))
		if(action >= 0 and action < 24):
			self.getAction(action, pturn=True)
			self.gameOver = True
		#for debug
		elif(action == -1):
			quit()
		else:
			self.getAction(action, pturn=True)
			print('P1 ACTIVE: ' + str(self.p1.getBoard().numberActive()))
			print('P2 ACTIVE: ' + str(self.p2.getBoard().numberActive()))
			if(self.p1.getBoard().numberActive() <= 1):
				self.p1.setScore(self.p1.getScore() + 1)
				print("PLAYER 1 WINS")
				self.status = 'WON'
				self.gameOver = True
		if(not self.gameOver):
			#the agent goes 
			action = random.randint(24, 42)
			print(self.p2.getName() + " is guessing" + str(action))
			if(action >= 0 and action < 24):
				self.getAction(action, pturn=False)
				self.gameOver = True
			#for debug
			elif(action == -1):
				quit()
			else:
				self.getAction(action, pturn=False)
				print("P1 ACTIVE: " + str(self.p1.getBoard().numberActive()))
				print("P2 ACTIVE: " + str(self.p2.getBoard().numberActive()))
				if(self.p2.getBoard().numberActive() <= 1):
					self.p2.setScore(self.p2.getScore() + 1)
					print("PLAYER 2 WINS")
					self.status = 'LOST'
					self.gameOver = True

			self.numTurns += 1
			print("TOTAL TURNS: " + str(self.numTurns))