import json
from types import SimpleNamespace

from call_function import call_function


def test_known_function_dispatch():
    """Test that a known function name dispatches successfully and returns real output."""
    tool_call = SimpleNamespace(
        id="call_123",
        function=SimpleNamespace(name="get_files_info", arguments='{"directory": "."}'),
    )
    
    result = call_function(tool_call)
    
    # Verify the result structure
    assert result["role"] == "tool"
    assert result["tool_call_id"] == "call_123"
    
    # Verify content contains real output (there should be files in the calculator directory)
    assert isinstance(result["content"], str)
    assert len(result["content"]) > 0
    # Should contain file listing information
    assert "file_size=" in result["content"] or "is_dir=" in result["content"]


def test_unknown_function_returns_error():
    """Test that an unknown function name returns an error message instead of raising an exception."""
    tool_call = SimpleNamespace(
        id="call_456",
        function=SimpleNamespace(name="not_a_real_function", arguments="{}"),
    )
    
    result = call_function(tool_call)
    
    # Verify the result structure
    assert result["role"] == "tool"
    assert result["tool_call_id"] == "call_456"
    
    # Verify content is an error message
    assert isinstance(result["content"], str)
    assert "Error: Unknown function:" in result["content"]


def test_result_structure_consistency():
    """Test that returned dict always has the correct structure for both known and unknown functions."""
    # Test with known function
    tool_call_known = SimpleNamespace(
        id="call_789",
        function=SimpleNamespace(name="get_files_info", arguments="{}"),
    )
    
    result_known = call_function(tool_call_known)
    
    # Test with unknown function
    tool_call_unknown = SimpleNamespace(
        id="call_012",
        function=SimpleNamespace(name="not_a_real_function", arguments="{}"),
    )
    
    result_unknown = call_function(tool_call_unknown)
    
    # Both should have the same structure
    for result in [result_known, result_unknown]:
        assert "role" in result
        assert "tool_call_id" in result
        assert "content" in result
        assert result["role"] == "tool"
        assert isinstance(result["tool_call_id"], str)
        assert isinstance(result["content"], str)


def test_arguments_without_working_directory():
    """Test that arguments without working_directory still work by forcing it to './calculator'."""
    tool_call = SimpleNamespace(
        id="call_345",
        function=SimpleNamespace(name="get_files_info", arguments='{"directory": "."}'),
    )
    
    result = call_function(tool_call)
    
    # Verify the result structure
    assert result["role"] == "tool"
    assert result["tool_call_id"] == "call_345"
    
    # Verify content contains real output about calculator directory contents
    assert isinstance(result["content"], str)
    assert len(result["content"]) > 0
    # Should contain file listing information
    assert "file_size=" in result["content"] or "is_dir=" in result["content"]