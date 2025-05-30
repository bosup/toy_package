import argparse
import numpy as np
from toy.api import AtmosphericRiverAnalyzer, RiverTrendDetector, RiverStatistics, RiverSummary

def main():
    parser = argparse.ArgumentParser(description="Atmospheric River Metrics CLI")
    parser.add_argument('--mode', choices=['intensity', 'trend', 'max', 'summary'], required=True)
    parser.add_argument('--data', nargs='+', type=float, required=True)
    args = parser.parse_args()

    data = np.array(args.data)

    if args.mode == 'intensity':
        result = AtmosphericRiverAnalyzer(data).calculate_intensity()
    elif args.mode == 'trend':
        result = RiverTrendDetector(data).detect_trend()
    elif args.mode == 'max':
        result = RiverStatistics(data).get_max()
    elif args.mode == 'summary':
        result = RiverSummary(data).summarize()

    print(result)

if __name__ == "__main__":
    main()
