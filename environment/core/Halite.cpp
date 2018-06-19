#include "Constants.hpp"
#include "BlurTileGenerator.hpp"
#include "Halite.hpp"
#include "HaliteImpl.hpp"
#include "Logging.hpp"

namespace hlt {

/** Run the game. */
void Halite::run_game() {
    for (auto &player : players) {
        networking.initialize_player(player.second);
    }
    const auto &constants = Constants::get();
    for (turn_number = 0; turn_number < constants.MAX_TURNS; turn_number++) {
        impl->process_commands(impl->retrieve_commands());
        impl->process_production();
        impl->process_entities();

        if (impl->game_ended()) {
            break;
        }
    }
    Logging::log("Game has ended after " + std::to_string(turn_number) + " turns.");
    // TODO: generate replay
    // TODO: thread the communications with players
}

/**
 * Constructor for the main game.
 *
 * @param config The configuration options for the game.
 * @param parameters The map generation parameters.
 * @param networking_config The networking configuration.
 * @param players The list of players.
 */
Halite::Halite(const Config &config,
               const mapgen::MapParameters &parameters,
               const net::NetworkingConfig &networking_config,
               std::list<Player> players) :
        config(config),
        parameters(parameters),
        networking(net::Networking(networking_config, this)),
        impl(std::make_unique<HaliteImpl>(this)),
        game_map(mapgen::BlurTileGenerator(parameters).generate(players)) {
    for (const auto &player : players) {
        this->players[player.player_id] = player;
        game_stats.player_statistics.emplace_back(player.player_id);
    }
}

/** Default destructor is defined where HaliteImpl is complete. */
Halite::~Halite() = default;

}
