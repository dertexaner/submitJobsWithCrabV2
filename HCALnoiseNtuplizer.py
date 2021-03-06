# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: RECO --data -s RAW2DIGI,RECO --filein file:/tmp/hsaka/Run2012B_HcalNZS_RAW_v1_000_197_305_50818EDA-68BF-E111-8D4D-001D09F24FBA.root --fileout DummyOutput.root --conditions PRE_R_72_V10A::All --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input files
#process.source.fileNames = [
    #Specified by InputList.txt
#]

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
#    fileNames = [
        #Specified by InputList.txt
#        ]
    fileNames = cms.untracked.vstring('')
    #fileNames = cms.untracked.vstring('file:/tmp/hsaka/Run2012B_HcalNZS_RAW_v1_000_197_305_50818EDA-68BF-E111-8D4D-001D09F24FBA.root')
    #
    #fileNames = cms.untracked.vstring('file:/tmp/hsaka/11_store_data_Run2012B_HcalNZS_RAW_v1_000_194_050_7CAABEF7-2A9C-E111-B938-BCAEC518FF6E.root')
    #fileNames = cms.untracked.vstring('file:/tmp/hsaka/11_store_data_Run2012B_HcalNZS_RAW_v1_000_194_076_9000FB9B-DF9C-E111-809A-001D09F2305C.root')
    #fileNames = cms.untracked.vstring('file:/tmp/hsaka/11_store_data_Run2012B_HcalNZS_RAW_v1_000_194_224_E058678F-FD9E-E111-9746-001D09F29619.root')
    #fileNames = cms.untracked.vstring('file:/tmp/hsaka/11_store_data_Run2012B_HcalNZS_RAW_v1_000_194_108_3A9C8542-459D-E111-AF00-0030486780B8.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('RECO nevts:1'),
    name = cms.untracked.string('Applications')
)

# Output definition

#process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
#    splitLevel = cms.untracked.int32(0),
#    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
#    outputCommands = process.RECOSIMEventContent.outputCommands,
#    fileName = cms.untracked.string('DummyOutput.root'),
#    dataset = cms.untracked.PSet(
#        filterName = cms.untracked.string(''),
#        dataTier = cms.untracked.string('')
#    )
#)


# Hcal noise analyzers
process.HBHENoiseFilterResultProducer = cms.EDProducer(
   'HBHENoiseFilterResultProducer',
   noiselabel = cms.InputTag('hcalnoise'),
   minRatio = cms.double(-999),
   maxRatio = cms.double(999),
   minHPDHits = cms.int32(17),
   minRBXHits = cms.int32(999),
   minHPDNoOtherHits = cms.int32(10),
   minZeros = cms.int32(10),
   minHighEHitTime = cms.double(-9999.0),
   maxHighEHitTime = cms.double(9999.0),
   maxRBXEMF = cms.double(-999.0),
   minNumIsolatedNoiseChannels = cms.int32(10),
   minIsolatedNoiseSumE = cms.double(50.0),
   minIsolatedNoiseSumEt = cms.double(25.0),
   useTS4TS5 = cms.bool(True),
   IgnoreTS4TS5ifJetInLowBVRegion = cms.bool(True),
   jetlabel = cms.InputTag('ak5PFJets'),
   maxjetindex = cms.int32(0),
   maxNHF = cms.double(0.9)
   )

process.TFileService = cms.Service("TFileService",
   fileName = cms.string( THISROOTFILE )
   #fileName = cms.string("NoiseTree.root")
   #fileName = cms.string("Run2012B_HcalNZS_RAW_v1_000_197_305_50818EDA-68BF-E111-8D4D-001D09F24FBA__NoiseTree.root")
   #
   #fileName = cms.string("11_store_data_Run2012B_HcalNZS_RAW_v1_000_194_050_7CAABEF7-2A9C-E111-B938-BCAEC518FF6E__NoiseTree.root")
   #fileName = cms.string("11_store_data_Run2012B_HcalNZS_RAW_v1_000_194_076_9000FB9B-DF9C-E111-809A-001D09F2305C__NoiseTree.root")
   #fileName = cms.string("11_store_data_Run2012B_HcalNZS_RAW_v1_000_194_224_E058678F-FD9E-E111-9746-001D09F29619__NoiseTree.root")
   #fileName = cms.string("11_store_data_Run2012B_HcalNZS_RAW_v1_000_194_108_3A9C8542-459D-E111-AF00-0030486780B8__NoiseTree.root")
   )

process.ExportTree = cms.EDAnalyzer("HcalNoiseAnalyzer",
   HBHERecHitCollection = cms.untracked.string('hbhereco')
   )


# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_R_53_V21', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'FT_P_V42D', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'PRE_R_72_V10A', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
#process.reconstruction_step = cms.Path(process.reconstruction)
process.reconstruction_step = cms.Path(process.reconstruction * process.HBHENoiseFilterResultProducer * process.ExportTree)
process.endjob_step = cms.EndPath(process.endOfProcess)
#process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
#process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step)


