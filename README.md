# Promraw - Prompt, Draw 🎨

## Introduction

Welcome to Promraw, an online game that brings together creativity and AI to score user-submitted digital drawings based on zany prompts! With Promraw, users can unleash their artistic talents while enjoying a fun and interactive experience.

## At a Glance

Promraw is like an AI sandwich with humans in the middle! Here's how it works:

1. **Silly Prompts**: Users are presented with amusing and quirky prompts such as "a shark in a barrel" or "the world's fastest frog."
   
2. **Drawing Time**: Users then draw their interpretation of the given prompt using our browser-based drawing tool powered by Literally Canvas.
   
3. **AI Scoring**: Once the drawing is submitted, our AI system, Paint, scores the drawing using CLIP, a model trained on image-text pairs. The closer the user's drawing is to the prompt's image representation according to CLIP, the higher the score.

## How We Generate Prompts

We didn't stop at just a few prompts; we used AI to generate thousands of creative prompts! Here's how:

- **Initial Prompts**: We started with a set of initial prompts.
  
- **AI Prompt Generation**: Leveraging GPT-2, a generative text model, we expanded our prompt collection to include thousands of unique and unexpected ideas.
  
- **Human Touch**: While AI generated most of the prompts, our team ensured that they all encouraged fun and creativity.

## Tech Stack Used

- **Flask**: Backend web framework for handling server-side logic.
  
- **TensorFlow & PyTorch**: Deep learning frameworks for AI model development.
  
- **CLIP**: AI model for scoring user drawings based on image-text pairs.
  
- **Vanilla JS**: JavaScript for interactive client-side functionalities.

## Future Updates

We have exciting plans to enhance Promraw even further:

- **NFT marketplace Integration**: Soon, users will be able to turn their digital drawings into non-fungible tokens (NFTs) and even sell them in our integrated NFT marketplace!
  
- **Content Moderation**: We're working on improving content moderation tools to ensure a positive and safe experience for all users.

## Contributing

Interested in contributing to Promraw? We welcome developers, designers, and anyone passionate about creativity and AI! Feel free to reach out to us or submit a pull request on GitHub.

## Feedback

We value your feedback! If you have any suggestions, questions, or just want to say hi, don't hesitate to contact us.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

🚀 Let's get creative with Promraw!🎨
