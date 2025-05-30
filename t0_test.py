from toy import AtmosphericRiverAnalyzer, RiverStatistics

data = [1.0, 2.0, 3.0]

analyzer = AtmosphericRiverAnalyzer(data)
print(analyzer.calculate_intensity())

stats = RiverStatistics(data)
print(stats.get_max())

