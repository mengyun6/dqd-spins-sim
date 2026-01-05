"""I/O utilities for saving results and configurations."""

import json
import yaml
import os
import numpy as np
from pathlib import Path
from typing import Dict, Any
import shutil


def create_output_directory(base_dir: str, run_id: str) -> Path:
    """
    Create a unique output directory for a simulation run.
    
    Args:
        base_dir: Base directory for results (e.g., "results")
        run_id: Unique identifier for this run
        
    Returns:
        Path to the created directory
    """
    output_dir = Path(base_dir) / run_id
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def save_config(config: Dict[str, Any], output_path: Path) -> None:
    """
    Save a configuration dictionary to a YAML file.
    
    Args:
        config: Configuration dictionary
        output_path: Path where the config should be saved
    """
    with open(output_path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)


def save_metrics(metrics: Dict[str, Any], output_path: Path) -> None:
    """
    Save simulation metrics to a JSON file.
    
    Args:
        metrics: Dictionary containing metrics to save
        output_path: Path where the metrics should be saved
    """
    # Convert numpy types to native Python types for JSON serialization
    def convert_to_serializable(obj):
        if isinstance(obj, dict):
            return {k: convert_to_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [convert_to_serializable(item) for item in obj]
        elif isinstance(obj, (np.integer, np.floating)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return obj
    
    serializable_metrics = convert_to_serializable(metrics)
    
    with open(output_path, 'w') as f:
        json.dump(serializable_metrics, f, indent=2)


def generate_run_id() -> str:
    """
    Generate a unique run identifier based on timestamp.
    
    Returns:
        String identifier in format: YYYYMMDD_HHMMSS
    """
    from datetime import datetime
    return datetime.now().strftime("%Y%m%d_%H%M%S")

