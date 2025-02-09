ElementData
===========

`WMA link <https://reference.wolfram.com/language/ref/ElementData.html>`_


:code:`ElementData` [":math:`name`", ":math:`property`"]
    gives the value of the :math:`property` for the chemical
    specified by :math:`name`.

:code:`ElementData` [:math:`n`, ":math:`property`"]
    gives the value of the :math:`property` for the :math:`n`-th chemical element.





>>> ElementData[74]

    =
:math:`\text{Tungsten}`


>>> ElementData["He", "AbsoluteBoilingPoint"]

    =
:math:`4.22`


>>> ElementData["Carbon", "IonizationEnergies"]

    =
:math:`\left\{1086.5,2352.6,4620.5,6222.7,37831,47277.\right\}`


>>> ElementData[16, "ElectronConfigurationString"]

    =
:math:`\text{[Ne] 3s2 3p4}`


>>> ElementData[73, "ElectronConfiguration"]

    =
:math:`\left\{\left\{2\right\},\left\{2,6\right\},\left\{2,6,10\right\},\left\{2,6,10,14\right\},\left\{2,6,3\right\},\left\{2\right\}\right\}`



The number of known elements:

>>> Length[ElementData[All]]

    =
:math:`118`



Some properties are not appropriate for certain elements:

>>> ElementData["He", "ElectroNegativity"]

    =
:math:`\text{Missing}\left[\text{NotApplicable}\right]`



Some data is missing:

>>> ElementData["Tc", "SpecificHeat"]

    =
:math:`\text{Missing}\left[\text{NotAvailable}\right]`



All the known properties:

>>> ElementData["Properties"]

    =
:math:`\left\{\text{Abbreviation},\text{AbsoluteBoilingPoint},\text{AbsoluteMeltingPoint},\text{AtomicNumber},\text{AtomicRadius},\text{AtomicWeight},\text{Block},\text{BoilingPoint},\text{BrinellHardness},\text{BulkModulus},\text{CovalentRadius},\text{CrustAbundance},\text{Density},\text{DiscoveryYear},\text{ElectroNegativity},\text{ElectronAffinity},\text{ElectronConfiguration},\text{ElectronConfigurationString},\text{ElectronShellConfiguration},\text{FusionHeat},\text{Group},\text{IonizationEnergies},\text{LiquidDensity},\text{MeltingPoint},\text{MohsHardness},\text{Name},\text{Period},\text{PoissonRatio},\text{Series},\text{ShearModulus},\text{SpecificHeat},\text{StandardName},\text{ThermalConductivity},\text{VanDerWaalsRadius},\text{VaporizationHeat},\text{VickersHardness},\text{YoungModulus}\right\}`


>>> ListPlot[Table[ElementData[z, "AtomicWeight"], {z, 118}]]

    =
.. image:: tmpjnsbtf19.png
    :align: center



