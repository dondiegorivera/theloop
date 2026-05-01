rivera@agentserver:/srv/compose/agentserver/litellm$ cat config.yaml config
model_list:
  - model_name: Qwen3.6-Mesh-Structured
    litellm_params:
      model: openai/Qwen3.6-35B-A3B-Q5KM-Vision-64k
      api_base: http://100.69.40.49:8080/v1
      api_key: none
      max_tokens: 4096
      temperature: 0.2
      top_p: 0.85
      presence_penalty: 0.0
      repetition_penalty: 1.0
      extra_body:
        top_k: 20
        min_p: 0.0
        reasoning_format: none
        reasoning_budget: 0
        chat_template_kwargs:
          enable_thinking: false
    model_info:
      description: "35B structured"
      max_input_tokens: 65536
      max_output_tokens: 4096
      mode: chat

  - model_name: Qwen3.6-Mesh
    litellm_params:
      model: openai/Qwen3.6-35B-A3B-Q5KM-Vision-64k
      api_base: http://100.69.40.49:8080/v1
      api_key: none
      max_tokens: 2048
      temperature: 0.7
      top_p: 0.8
      presence_penalty: 1.5
      repetition_penalty: 1.0
      extra_body:
        top_k: 20
        min_p: 0.0
        reasoning_format: none
        reasoning_budget: 0
        chat_template_kwargs:
          enable_thinking: false
    model_info:
      description: "35B fast QA"
      max_input_tokens: 65536
      max_output_tokens: 2048
      mode: chat

  - model_name: Qwen3.6-Mesh-Thinking
    litellm_params:
      model: openai/Qwen3.6-35B-A3B-Q5KM-Vision-64k
      api_base: http://100.69.40.49:8080/v1
      api_key: none
      max_tokens: 4096
      temperature: 1.0
      top_p: 0.95
      presence_penalty: 1.5
      repetition_penalty: 1.0
      extra_body:
        top_k: 20
        min_p: 0.0
        reasoning_format: deepseek
        reasoning_budget: 2048
        chat_template_kwargs:
          enable_thinking: true
    model_info:
      description: "35B thinking"
      max_input_tokens: 65536
      max_output_tokens: 4096
      mode: chat

  - model_name: Qwen3.6-Mesh-Thinking-Long
    litellm_params:
      model: openai/Qwen3.6-35B-A3B-Q5KM-Vision-64k
      api_base: http://100.69.40.49:8080/v1
      api_key: none
      max_tokens: 16384
      temperature: 0.3
      top_p: 0.85
      presence_penalty: 0.3
      repetition_penalty: 1.0
      extra_body:
        top_k: 20
        min_p: 0.0
        reasoning_format: deepseek
        reasoning_budget: 4096
        chat_template_kwargs:
          enable_thinking: true
    model_info:
      description: "35B long stable"
      max_input_tokens: 65536
      max_output_tokens: 16384
      mode: chat

  - model_name: Qwen3.6-Mesh-Creative-Long
    litellm_params:
      model: openai/Qwen3.6-35B-A3B-Q5KM-Vision-64k
      api_base: http://100.69.40.49:8080/v1
      api_key: none
      max_tokens: 32768
      temperature: 1
      top_p: 0.95
      presence_penalty: 1.5
      repetition_penalty: 1.05
      extra_body:
        top_k: 20
        min_p: 0.05
        reasoning_format: deepseek
        reasoning_budget: 8192
        chat_template_kwargs:
          enable_thinking: true
    model_info:
      description: "35B creative long"
      max_input_tokens: 229376
      max_output_tokens: 32768
      mode: chat

  - model_name: Qwen3.6-Mesh-Code-Long
    litellm_params:
      model: openai/Qwen3.6-35B-A3B-Q5KM-Vision-64k
      api_base: http://100.69.40.49:8080/v1
      api_key: none
      max_tokens: 32768
      temperature: 0.2
      top_p: 0.9
      presence_penalty: 0.0
      repetition_penalty: 1.1
      extra_body:
        top_k: 20
        min_p: 0.0
        reasoning_format: deepseek
        reasoning_budget: 8192
        chat_template_kwargs:
          enable_thinking: true
    model_info:
      description: "35B coding long"
      max_input_tokens: 229376
      max_output_tokens: 32768
      mode: chat

//

model_list:
  - model_name: Qwen3.6-Mesh-Structured
    litellm_params:
      model: openai/Qwen3.6-27B-Q5KXL-87k-p3-q8
      api_base: http://100.69.40.49:8080/v1
      api_key: none
      max_tokens: 4096
      temperature: 0.2
      top_p: 0.85
      presence_penalty: 0.0
      repetition_penalty: 1.0
      extra_body:
        top_k: 20
        min_p: 0.0
        repeat_penalty: 1.0
        reasoning_format: none
        reasoning_budget: 0
        chat_template_kwargs:
          enable_thinking: false
    model_info:
      description: "27B structured/director"
      max_input_tokens: 87552
      max_output_tokens: 4096
      mode: chat

  - model_name: Qwen3.6-Mesh
    litellm_params:
      model: openai/Qwen3.6-27B-Q5KXL-87k-p3-q8
      api_base: http://100.69.40.49:8080/v1
      api_key: none
      max_tokens: 3072
      temperature: 0.7
      top_p: 0.8
      presence_penalty: 1.5
      repetition_penalty: 1.0
      extra_body:
        top_k: 20
        min_p: 0.0
        reasoning_format: none
        reasoning_budget: 0
        chat_template_kwargs:
          enable_thinking: false
    model_info:
      description: "27B fast QA"
      max_input_tokens: 87552
      max_output_tokens: 3072
      mode: chat

  - model_name: Qwen3.6-Mesh-Thinking
    litellm_params:
      model: openai/Qwen3.6-27B-Q5KXL-87k-p3-q8
      api_base: http://100.69.40.49:8080/v1
      api_key: none
      max_tokens: 6144
      temperature: 1.0
      top_p: 0.95
      presence_penalty: 1.5
      repetition_penalty: 1.0
      extra_body:
        top_k: 20
        min_p: 0.0
        reasoning_format: deepseek
        reasoning_budget: 2048
        chat_template_kwargs:
          enable_thinking: true
    model_info:
      description: "27B thinking agent"
      max_input_tokens: 87552
      max_output_tokens: 6144
      mode: chat

  - model_name: Qwen3.6-Mesh-Thinking-Long
    litellm_params:
      model: openai/Qwen3.6-27B-Q5KXL-87k-p3-q8
      api_base: http://100.69.40.49:8080/v1
      api_key: none
      max_tokens: 12288
      temperature: 0.3
      top_p: 0.85
      presence_penalty: 0.3
      repetition_penalty: 1.0
      extra_body:
        top_k: 20
        min_p: 0.0
        reasoning_format: deepseek
        reasoning_budget: 4096
        chat_template_kwargs:
          enable_thinking: true
    model_info:
      description: "27B long stable generation"
      max_input_tokens: 87552
      max_output_tokens: 12288
      mode: chat

  - model_name: Qwen3.6-Mesh-Creative-Long
    litellm_params:
      model: openai/Qwen3.6-27B-Q5KXL-87k-p3-q8
      api_base: http://100.69.40.49:8080/v1
      api_key: none
      max_tokens: 32768
      temperature: 1.0
      top_p: 0.95
      presence_penalty: 1.5
      repetition_penalty: 1.05
      extra_body:
        top_k: 20
        min_p: 0.05
        reasoning_format: deepseek
        reasoning_budget: 8192
        chat_template_kwargs:
          enable_thinking: true
    model_info:
      description: "27B creative long"
      max_input_tokens: 229376
      max_output_tokens: 32768
      mode: chat

  - model_name: Qwen3.6-Mesh-Code-Long
    litellm_params:
      model: openai/Qwen3.6-27B-Q5KXL-87k-p3-q8
      api_base: http://100.69.40.49:8080/v1
      api_key: none
      max_tokens: 32768
      temperature: 0.2
      top_p: 0.9
      presence_penalty: 0.0
      repetition_penalty: 1.1
      extra_body:
        top_k: 20
        min_p: 0.0
        reasoning_format: deepseek
        reasoning_budget: 8192
        chat_template_kwargs:
          enable_thinking: true
    model_info:
      description: "27B coding long"
      max_input_tokens: 229376
      max_output_tokens: 32768
      mode: chat