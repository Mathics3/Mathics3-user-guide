SphericalHarmonicY
==================

`Spherical Harmonic https <//mathworld.wolfram.com/SphericalHarmonic.html>`_ (`mpmath <https://mpmath.org/doc/current/functions/orthogonal.html#mpmath.sperharm>`_, `WMA <https://reference.wolfram.com/language/ref/SphericalHarmonicY.html>`_)

:code:`SphericalHarmonicY` [:math:`l`, :math:`m`, :math:`\theta`, :math:`\phi`]
    returns the spherical harmonic function :math:`Y_l^m(\theta, \phi)`.





>>> SphericalHarmonicY[3/4, 0.5, Pi/5, Pi/3]

    =
:math:`0.254247+0.14679 I`


>>> SphericalHarmonicY[3, 1, theta, phi]

    =
:math:`\frac{\sqrt{21} \left(1-5 \text{Cos}\left[\text{theta}\right]^2\right) E^{I \text{phi}} \text{Sin}\left[\text{theta}\right]}{8 \sqrt{ \pi }}`


