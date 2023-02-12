from present import Config, Timing, Present

present = Present(
    title="vbvps1: block time & proof time both go down, up to the SAME direction, then restores",
    desc="""

""",
    days=21,
    config=Config(
        max_blocks=2048, 
        lamda=590,
        fee_base=100.0,
        fee_maf=1024,
        reward_multiplier=4.0,
        time_avg_maf=1024,
        block_time_sd_pctg=0,
        proof_time_sd_pctg=0,
        timing=[
            Timing(
                block_time_avg_second=15,
                proof_time_avg_minute=45,
            ),
            Timing(
                block_time_avg_second=15/1.3,
                proof_time_avg_minute=45/1.3,
            ),
            Timing(
                block_time_avg_second=15/1.3/1.3,
                proof_time_avg_minute=45/1.3/1.3,
            ),
            Timing(
                block_time_avg_second=15/1.3,
                proof_time_avg_minute=45/1.3,
            ),
            Timing(
                block_time_avg_second=15,
                proof_time_avg_minute=45,
            ),
            Timing(
                block_time_avg_second=15*1.3,
                proof_time_avg_minute=45*1.3,
            ),
            Timing(
                block_time_avg_second=15*1.3*1.3,
                proof_time_avg_minute=45*1.3*1.3,
            ),
            Timing(
                block_time_avg_second=15*1.3,
                proof_time_avg_minute=45*1.3,
            ),
            Timing(
                block_time_avg_second=15,
                proof_time_avg_minute=45,
            ),
        ],
    ),
)
