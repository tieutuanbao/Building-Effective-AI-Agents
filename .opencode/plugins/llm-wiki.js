// llm-wiki OpenCode plugin
// Injects a wiki reminder before bash tool calls when wiki/ exists.
// Install: add to opencode.json plugins array + mkdir -p .opencode/plugins
import { existsSync } from "fs";
import { join } from "path";

export const LlMWikiPlugin = async ({ directory }) => {
  let reminded = false;

  return {
    "tool.execute.before": async (input, output) => {
      if (reminded) return;
      if (!existsSync(join(directory, "wiki", "SUMMARY.md"))) return;

      if (input.tool === "bash") {
        output.args.command =
          'echo "[llm-wiki] Knowledge wiki exists. Read wiki/SUMMARY.md for quick overview, or run /llm-wiki query to explore." && ' +
          output.args.command;
        reminded = true;
      }
    },
  };
};