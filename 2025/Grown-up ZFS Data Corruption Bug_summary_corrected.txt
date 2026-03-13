• Discussion about a data corruption bug being 18 years old and "all grown up"
• Reference to a previous podcast episode on crucible and its potential data corruption issues
• Explanation of the initial issue with a failure to decrypt a block, indicating potential data corruption
• Analysis of the problem and discovery of a 32k extent with all zeros
• Discussion of the oxide storage service and its use of ZFS and redundant storage
• Explanation of a recent system update and its potential impact on the issue
• Discussion of the limitations of testing, specifically the lack of power-off/power-on testing
• Acknowledgement of the complexity of the issue and the need for further analysis
• Data corruption was suspected, but the cause was unclear
• The team found a single case of corruption in a file, which helped to isolate the issue
• The corruption was 32k of zeros at the start of the file
• A verify tool was created to check for the corruption in other files
• The team found only one failure case, which was a relief, but also raised concerns about other potential issues
• The team considered the possibility of data corruption being caused by an external factor, rather than their own code
• The team used a technique of stuffing additional data into spare bytes in the crucible extent files to gather more information about the corruption
• This technique was seen as a way to gather more information, rather than a fix for the bug itself
• The importance of having agency when dealing with system failures and corruption
• The design of Crucible's block-oriented storage and encryption metadata, including the use of slots to ensure data integrity
• The introduction of the flush number, which provides ordering information for blocks on disk
• The discovery of the "bonus data corruption bug" through a Jensen-style test
• The affidavit, a previously written document that outlines ordering guarantees for CFS, and its relationship to the bugs found in Crucible
• The mis implementation of the affidavit's terms in Crucible, leading to data corruption and failures to decrypt
• ZFS writes can introduce ordering issues due to delayed logging
• The delayed logging mechanism can lead to data corruption, such as 32k of zeros at the beginning of a file
• The issue is similar to a past bug related to the Silicon Image controller
• The team is trying to recall details of a past bug, but memories are hazy
• It's suggested that the bug may be related to a DMA controller issue, possibly with Silicon Image
• The conversation is lighthearted and humorous, with the team poking fun at their own forgetfulness
• Discussion of a previously reported data corruption bug and its resolution
• Bryan Can trill mentions that Matt Keeper had made a scanner to test for data corruption
• Adam Levinthal recalls a similar experience with data corruption at Delphi
• The group continues to test and scan for data corruption, including scanning "dog food" (an internal testing instance)
• The bonus data corruption bug is fixed, but the group is still experiencing issues
• The group continues to update and test the new code, with some issues still arising
• The process is ongoing, and the group is still refining their testing and debugging process.
• Investigating a corruption issue with a specific bug being ruled out
• Narrowing down the cause of the corruption to a power cycle during a repair process
• Understanding that the corruption requires a specific sequence of events: repair and power loss
• Reproducing the corruption on the Rocklike and having a high success rate
• Recognizing the unique "fingerprint" of the corruption (32k of zeros)
• Exploring possible causes and trying different approaches to resolve the issue
• Reflecting on the investigation process and the importance of learning from "false trails" and trial-and-error experimentation
• Discussion of ZFS immediate right size value being changed from 32k to 16k
• Exploration of the possibility of a "crucible bug" in ZFS and the team's investigation into its causes
• Realization that the issue may not be specific to Crucible, but rather a deeper problem in ZFS
• James McMahon's discovery of a small program that can reproduce the issue, isolating the problem to a specific interaction between ZFS and the hypervisor
• Confirmation that the issue is not related to Crucible, but rather a fundamental problem with ZFS behaviour in certain power-off scenarios
• Rust's behaviour was initially suspected to be the issue, but a C program was created to reproduce the problem
• The problem was found to be a ZFS bug, specifically with the ZIL (ZFS intent log)
• The issue was caused by transactions being replayed in the wrong order after a reboot, leading to corruption
• The problem was solved by understanding that the transactions were being put into the ZIL as if they were synchronous, but were actually asynchronous, and were being reordered during commit
• The optimization responsible for this issue was introduced in Polaris in 2007
• Discussion of Sun's Cool Threads technology and its limitations, including one FPU per core.
• Issue with slow f syncs in a hot lock, leading to data corruption in ZFS.
• Solution proposed, which involves logging writes as if they were synchronous.
• Concerns about the complexity and potential for data corruption.
• Discussion of the removal of the issue from Open ZFS and its reinstatement due to performance effects.
• Memories of the era of ZFS development and the need for benchmarking and heuristic tweaks.
• The ZFS subsystem has a unable variable "number four" that was set to a specific value in the past, without a clear understanding of its purpose or impact on system performance.
• This variable was set to optimize performance on specific hardware configurations, but its value was not based on a thorough understanding of the underlying system behaviour.
• The variable was left in place for many years, and its presence was only discovered recently due to a bug report and subsequent analysis.
• The variable has since been tested and found to have no positive impact on system performance, and setting it to zero has not caused any issues.
• The discussion highlights the importance of understanding the underlying system behaviour and avoiding the use of arbitrary unable variables in favour of more comprehensive and principled approaches to system design.
• Discussion of a unable being set to zero to address a system issue
• Analysis of potential performance risks and the conclusion that it's not a performance regression
• Explanation of the system's behaviour and its implications on performance
• Description of further analysis and optimization work done to address the issue
• Results of benchmarks showing a 2% change in F Sync performance
• Discussion of the importance of correctness in a specific code path (crucible repair operation)
• Reflection on the team's process and the value of collaboration in resolving issues
• Lessons learned from a pathology in a system, including not ignoring issues and trying to identify vulnerabilities.
• Importance of sharing information and collaboration to address data corruption.
• Value of the affidavit in understanding and fixing the issue.
• Discussion of a specific bug and its analysis.
• Parable of a DMA issue from 20+ years ago and its possible implantation in Bryan's memory.
• Humour and lightheartedness in the discussion of the issue.