import commands2
import wpilib


class RobotContainer:
	def __init__(self, isReal: bool):
		# TODO: subsystems
		self.robotDrive = None
		self.configureButtonBindings()
		self.driverController = wpilib.XboxController(0)
		# TODO: robotDrive.setDefaultCommand

	def configureButtonBindings(self) -> None:
		pass

	def getAutonomousCommand(self) -> commands2.Command:
		return commands2.InstantCommand()
