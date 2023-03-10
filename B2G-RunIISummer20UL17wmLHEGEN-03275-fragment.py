import FWCore.ParameterSet.Config as cms


externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring(<GRIDPACKS>),
    nEvents = cms.untracked.uint32(<NEVENTS>),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    generateConcurrently = cms.untracked.bool(True)
    )


#Link to datacards: /afs/cern.ch/work/a/agapitos/public/MC4/DMsimp_s_spin1/InputCards/

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8ConcurrentHadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
      pythia8CommonSettingsBlock,
      pythia8CP5SettingsBlock,
      pythia8aMCatNLOSettingsBlock,
      pythia8PSweightsSettingsBlock,
      parameterSets = cms.vstring(
        'pythia8CommonSettings',
        'pythia8CP5Settings',
        'pythia8aMCatNLOSettings',
        'pythia8PSweightsSettings',
        )
      )
    )
