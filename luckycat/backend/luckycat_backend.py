from luckycat.backend import CrashReceiver
from luckycat.backend import CrashVerificationCollector
from luckycat.backend import CrashVerificationSender
from luckycat.backend import JobScheduler
from luckycat.backend import SampleGenerator
from luckycat.backend import StatsCollector


def main():
    generator = SampleGenerator.SampleGenerator()
    crash_verification_sender = CrashVerificationSender.CrashVerificationSender()
    crash_verification_collector = CrashVerificationCollector.CrashVerificationCollector()
    stats_collector = StatsCollector.StatsCollector()
    crash_receiver = CrashReceiver.CrashReceiver()
    job_scheduler = JobScheduler.JobScheduler()

    generator.start()
    crash_verification_collector.start()
    crash_verification_sender.start()
    stats_collector.start()
    crash_receiver.start()
    job_scheduler.start()

    generator.join()
    crash_verification_collector.join()
    crash_verification_sender.join()
    stats_collector.join()
    crash_receiver.join()
    job_scheduler.join()


if __name__ == '__main__':
    main()
