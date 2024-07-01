import { QueryConfig } from '../config';
import { SpecQueryModel } from '../model';
import { Schema } from '../schema';
import { RankingScore } from './ranking';
export declare const name = "aggregationQuality";
export declare function score(specM: SpecQueryModel, schema: Schema, opt: QueryConfig): RankingScore;
