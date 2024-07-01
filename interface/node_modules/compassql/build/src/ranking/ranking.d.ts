import { QueryConfig } from '../config';
import { SpecQueryModel, SpecQueryModelGroup } from '../model';
import { Query } from '../query/query';
import { Dict } from '../util';
import { Schema } from '../schema';
export * from './effectiveness';
import * as aggregation from './aggregation';
import * as fieldOrder from './fieldorder';
export { aggregation, fieldOrder };
export interface RankingScore {
    score: number;
    features: FeatureScore[];
}
export interface FeatureScore {
    score: number;
    type: string;
    feature: string;
}
export interface FeatureInitializer {
    (): Dict<number>;
}
export interface Featurizer {
    (specM: SpecQueryModel, schema: Schema, opt: QueryConfig): FeatureScore[];
}
export interface FeatureFactory {
    type: string;
    init: FeatureInitializer;
    getScore: Featurizer;
}
export interface RankingFunction {
    (specM: SpecQueryModel, schema: Schema, opt: QueryConfig): RankingScore;
}
/**
 * Add an ordering function to the registry.
 */
export declare function register(name: string, keyFn: RankingFunction): void;
export declare function get(name: string): RankingFunction;
export declare function rank(group: SpecQueryModelGroup, query: Query, schema: Schema, level: number): SpecQueryModelGroup;
export declare function comparatorFactory(name: string | string[], schema: Schema, opt: QueryConfig): (m1: SpecQueryModel, m2: SpecQueryModel) => number;
export declare function groupComparatorFactory(name: string | string[], schema: Schema, opt: QueryConfig): (g1: SpecQueryModelGroup, g2: SpecQueryModelGroup) => number;
export declare function getScore(model: SpecQueryModel, rankingName: string, schema: Schema, opt: QueryConfig): RankingScore;
export declare const EFFECTIVENESS = "effectiveness";
