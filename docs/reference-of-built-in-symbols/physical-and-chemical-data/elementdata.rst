ElementData
===========

`WMA link <https://reference.wolfram.com/language/ref/ElementData.html>`_


:code:`ElementData` [":math:`name`", ":math:`property`"]
    gives the value of the :math:`property` for the chemical
    specified by :math:`name`.

:code:`ElementData` [:math:`n`, ":math:`property`"]
    gives the value of the :math:`property` for the :math:`n`-th chemical element.





>>> ElementData[74]
  = Tungsten
>>> ElementData["He", "AbsoluteBoilingPoint"]
  = 4.22
>>> ElementData["Carbon", "IonizationEnergies"]
  = {1086.5, 2352.6, 4620.5, 6222.7, 37831, 47277.}
>>> ElementData[16, "ElectronConfigurationString"]
  = [Ne] 3s2 3p4
>>> ElementData[73, "ElectronConfiguration"]
  = {{2}, {2, 6}, {2, 6, 10}, {2, 6, 10, 14}, {2, 6, 3}, {2}}

The number of known elements:

>>> Length[ElementData[All]]
  = 118

Some properties are not appropriate for certain elements:

>>> ElementData["He", "ElectroNegativity"]
  = Missing[NotApplicable]

Some data is missing:

>>> ElementData["Tc", "SpecificHeat"]
  = Missing[NotAvailable]

All the known properties:

>>> ElementData["Properties"]
  = {Abbreviation, AbsoluteBoilingPoint, AbsoluteMeltingPoint, AtomicNumber, AtomicRadius, AtomicWeight, Block, BoilingPoint, BrinellHardness, BulkModulus, CovalentRadius, CrustAbundance, Density, DiscoveryYear, ElectroNegativity, ElectronAffinity, ElectronConfiguration, ElectronConfigurationString, ElectronShellConfiguration, FusionHeat, Group, IonizationEnergies, LiquidDensity, MeltingPoint, MohsHardness, Name, Period, PoissonRatio, Series, ShearModulus, SpecificHeat, StandardName, ThermalConductivity, VanDerWaalsRadius, VaporizationHeat, VickersHardness, YoungModulus}
>>> ListPlot[Table[ElementData[z, "AtomicWeight"], {z, 118}]]
  = -Graphics-
