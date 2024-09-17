"""Module defining Materials Virtual Lab (MVL) VASP input set generators."""

from __future__ import annotations

import logging
from dataclasses import dataclass

from pymatgen.io.vasp.sets import MVLGWSet

logger = logging.getLogger(__name__)


@dataclass
class MVLGWSetGenerator(MVLGWSet):
    """
    Materials Virtual Lab GW input set generator.

    To generate Materials Virtual Lab input sets for static,
    diag and GW calculations.

    Parameters
    ----------
    mode
        The mode of the calculation. Options are "STATIC", "DIAG", and "GW".
    nbands_factor
        Multiplicative factor for NBANDS when starting from a previous calculation.
        Choose a higher number if you are doing an LOPTICS calculation.
    **kwargs
        Other keyword arguments that will be passed to :obj:`VaspInputGenerator`
    """

    reciprocal_density: float = 100
    mode: str = "STATIC"
    copy_wavecar: bool = True

    @property
    def incar_updates(self) -> dict:
        """Get updates to the INCAR for a Materials Virtual Lab GW calculation.

        Returns
        -------
        dict
            A dictionary of updates to apply.
        """
        return super().incar_updates
