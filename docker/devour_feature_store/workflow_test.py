import logging
from datetime import datetime
from time import perf_counter as pc
import numpy as np
import pandas as pd
from feast import FeatureStore
from feast.data_source import PushMode
from tqdm import tqdm

logging.basicConfig(level=logging.DEBUG)


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = pc()
        logging.info(f"Starting {func.__name__}...")
        result = func(*args, **kwargs)
        end_time = pc()
        time_elapsed = end_time - start_time
        hours, remainder = divmod(time_elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)
        logging.info(
            f"{func.__name__} took: {hours:.0f} hours {minutes:.2f} minutes and {seconds:.2f} seconds."
        )
        return result

    return wrapper


class TestFeatureStore:
    def __init__(self):
        self.fs = FeatureStore()

    @timing
    def run_test_cat(self, mode="online"):
        n = 1_000_000

        # Sequential product IDs from 900001 to 920000
        product_ids = np.arange(9_000_001, 9_000_001 + n)

        # Generate random general scores between 0 and 1
        general_scores = np.random.random(size=n)

        # Use today's timestamp for all events
        event_timestamp = datetime.now()

        # Build the DataFrame
        df = pd.DataFrame(
            {
                "product_id": product_ids,
                "general_score": general_scores,
                "general_score_1": general_scores,
                "general_score_2": general_scores,
                "general_score_3": general_scores,
                "general_score_4": general_scores,
                "general_score_5": general_scores,
                "general_score_6": general_scores,
                "general_score_7": general_scores,
                "general_score_8": general_scores,
                "general_score_9": general_scores,
                "general_score_10": general_scores,
                "event_timestamp": [event_timestamp] * n,
            }
        )

        self.fs.push(
            push_source_name="ds_push_product_general_score",
            df=df,
            to=PushMode.ONLINE if mode == "online" else PushMode.ONLINE_AND_OFFLINE,
        )

    @timing
    def run_test_bestseller_ethnicity(self, mode="online"):
        df = pd.read_parquet(
            "data/bestseller_features/product_bestseller_ethnicity_tag.parquet"
        )

        self.fs.push(
            push_source_name="ds_push_product_bestseller_ethnicity_tag",
            df=df,
            to=PushMode.ONLINE if mode == "online" else PushMode.ONLINE_AND_OFFLINE,
        )

    @timing
    def run_test_bestseller_propensity(self, mode="online"):
        df = pd.read_parquet("data/bestseller_features/user_propensity_score.parquet")
        print(f" df read, with shape {df.shape}")

        for chunk in tqdm(range(0, df.shape[0], 10_000)):
            self.fs.push(
                push_source_name="ds_push_user_propensity_score",
                df=df.iloc[chunk : chunk + 10_000],
                to=PushMode.ONLINE if mode == "online" else PushMode.ONLINE_AND_OFFLINE,
            )


if __name__ == "__main__":
    # run_test_cat()
    t = TestFeatureStore()
    t.run_test_bestseller_ethnicity()
    t.run_test_bestseller_propensity()
